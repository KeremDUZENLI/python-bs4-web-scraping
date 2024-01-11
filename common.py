import csv

csv_file_name = "results.csv"
output_csv_file = "results_common.csv"

website_words = {}
with open(csv_file_name, mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)

    current_website = None
    website_word_list = []

    for row in reader:
        if 'WEB Adress' in row:
            if current_website:
                website_words[current_website] = website_word_list

            current_website = row[1]
            website_word_list = []

        elif len(row) == 2 and row[0] and row[1].isdigit():
            word, _ = row
            website_word_list.append(word)

    if current_website:
        website_words[current_website] = website_word_list

common_words_tracker = {word: set()
                        for word in set.union(*map(set, website_words.values()))}

for website, words in website_words.items():
    for word in words:
        common_words_tracker[word].add(website)

common_words_between_websites = {
    word: websites for word, websites in common_words_tracker.items() if len(websites) >= 2}

sorted_common_words = sorted(common_words_between_websites.items(
), key=lambda x: (len(x[1]), x[0]), reverse=True)

with open(output_csv_file, mode='w', encoding='utf-8', newline='') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerow(['Common Word', 'Websites'])

    for word, websites in sorted_common_words:
        writer.writerow([word, ', '.join(sorted(websites))])

print(f"Common words among websites saved to {output_csv_file}")
