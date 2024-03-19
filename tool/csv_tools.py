import csv
from web.web_translator import words_translate_deepl


def create_csv_words_frequency(common_words_list, output_csv):
    with open(output_csv, mode='w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Most Common Words', 'Frequency'])
        writer.writerow([])

        for common_words in common_words_list:
            website_url = common_words['WEB Adress']
            top_words = common_words['Top Words']

            writer.writerow(['WEB Adress', website_url])

            for word, freq in top_words:
                writer.writerow([word, freq])

            writer.writerow([])


def create_csv_words_translated(input_csv, output_csv, target_language, deepl_auth_key):
    website_words_dict = read_csv_each_website(input_csv)

    with open(output_csv, mode='w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Most Common Words', 'Frequency'])
        writer.writerow([])

        for website_url, words_list in website_words_dict.items():
            writer.writerow(['WEB Adress', website_url])

            for word, freq in words_list.items():
                translated_word = words_translate_deepl(
                    word, target_language, deepl_auth_key)
                writer.writerow([translated_word, freq])

            writer.writerow([])


def create_csv_words_common(input_csv, output_csv):
    common_words_dict = read_csv_each_website(input_csv)

    common_words_tracker = {word: set()
                            for word in set.union(*map(set, common_words_dict.values()))}

    for website, words in common_words_dict.items():
        for word, freq in words.items():
            common_words_tracker[word].add((website, freq))

    common_words_between_websites = {
        word: websites for word, websites in common_words_tracker.items() if len(websites) >= 2}

    sorted_common_words = sorted(common_words_between_websites.items(),
                                 key=lambda x: (len(x[1]), max(x[1], key=lambda y: y[1])[1], x[0]), reverse=True)

    with open(output_csv, mode='w', encoding='utf-8', newline='') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['Common Word', 'Total Frequency', 'Websites'])

        for word, websites_freq in sorted_common_words:
            websites = ', '.join(
                sorted([f"{site} ({freq})" for site, freq in websites_freq]))
            total_frequency = sum(freq for _, freq in websites_freq)
            writer.writerow([word, total_frequency, websites])


def read_csv_each_website(input_csv):
    website_words_dict = {}
    with open(input_csv, mode='r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)

        current_website = None
        website_word_freq_dict = {}

        for row in reader:
            if 'WEB Adress' in row:
                if current_website:
                    website_words_dict[current_website] = website_word_freq_dict

                current_website = row[1]
                website_word_freq_dict = {}

            elif len(row) == 2 and row[0] and row[1].isdigit():
                word, freq = row
                website_word_freq_dict[word] = int(freq)

        if current_website:
            website_words_dict[current_website] = website_word_freq_dict

    return website_words_dict
