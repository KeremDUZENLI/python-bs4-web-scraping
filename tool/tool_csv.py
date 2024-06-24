import csv
from tool.tool import calculate_common_words_tracker, sort_common_words


def create_common_words_among_websites_dict_to_csv(all_websites_frequent_words_dict, output_csv):
    common_words_tracker = calculate_common_words_tracker(
        all_websites_frequent_words_dict)
    sorted_common_words = sort_common_words(common_words_tracker)

    with open(output_csv, mode='w', encoding='utf-8', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Common Word', 'Total Frequency', 'Websites'])

        for word, websites_freq in sorted_common_words:
            websites = ', '.join(
                sorted([f"{site} ({freq})" for site, freq in websites_freq]))
            total_frequency = sum(freq for _, freq in websites_freq)
            writer.writerow([word, total_frequency, websites])


def create_all_websites_frequent_words_dict_to_csv(all_websites_frequent_words_dict, output_csv):
    with open(output_csv, mode='w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Most Frequent Words', 'Frequency'])
        writer.writerow([])

        for website_common_words_dict in all_websites_frequent_words_dict:
            website_url = website_common_words_dict['WEB Adress']
            top_words = website_common_words_dict['Top Words']

            writer.writerow([website_url])

            if top_words is not None:
                for word, freq in top_words:
                    writer.writerow([word, freq])

            writer.writerow([])


def save_unreached_websites_dict_as_csv(class_instance):
    create_unreached_websites_dict_to_csv(
        class_instance.unreached_websites_dict, class_instance.unreached_websites_dict_csv)


def create_unreached_websites_dict_to_csv(unreached_websites_dict, output_csv):
    with open(output_csv, mode='w', encoding='utf-8', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Website', 'Error'])

        for website, error in unreached_websites_dict:
            writer.writerow([website, error])
