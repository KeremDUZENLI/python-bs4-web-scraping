import pandas as pd
from web.web_translator import words_translate_deepl


def create_excel_words_frequency(common_words_list, output_excel):
    df = pd.DataFrame(columns=['WEB Adress', 'Most Common Words', 'Frequency'])

    for common_words in common_words_list:
        website_url = common_words['WEB Adress']
        top_words_and_frequency = common_words['Top Words']

        website_df = pd.DataFrame(top_words_and_frequency, columns=[
                                  'Most Common Words', 'Frequency'])
        website_df['WEB Adress'] = website_url

        df = pd.concat([df, website_df], ignore_index=True)

    df.to_excel(output_excel, index=False)


def create_excel_words_translated(input_excel, output_excel, target_language, deepl_auth_key):
    website_words_dict = read_excel_each_website(input_excel)

    translated_website_words_dict = {}
    for website_url, words_list in website_words_dict.items():
        translated_words_list = []
        for word, freq in words_list:
            translated_word = words_translate_deepl(
                word, target_language, deepl_auth_key)
            translated_words_list.append((translated_word, freq))
        translated_website_words_dict[website_url] = translated_words_list

    df = pd.DataFrame(columns=['WEB Adress', 'Most Common Words', 'Frequency'])
    for website_url, words_list in translated_website_words_dict.items():
        website_df = pd.DataFrame(
            words_list, columns=['Most Common Words', 'Frequency'])
        website_df['WEB Adress'] = website_url
        df = pd.concat([df, website_df], ignore_index=True)

    df.to_excel(output_excel, index=False)


def create_excel_words_common(input_excel, output_excel):
    website_words_dict = read_excel_each_website(input_excel)

    common_words_tracker = {}

    for website, words in website_words_dict.items():
        for word, freq in words:
            if word not in common_words_tracker:
                common_words_tracker[word] = []
            common_words_tracker[word].append((website, freq))

    common_words_between_websites = {
        word: websites for word, websites in common_words_tracker.items() if len(websites) >= 2}

    sorted_common_words = sorted(common_words_between_websites.items(),
                                 key=lambda x: (len(x[1]), max(x[1], key=lambda y: y[1])[1], x[0]), reverse=True)

    rows = []
    for word, websites_freq in sorted_common_words:
        websites = ', '.join(
            sorted([f"{site} ({freq})" for site, freq in websites_freq]))
        total_frequency = sum(freq for _, freq in websites_freq)
        rows.append(
            {'Common Word': word, 'Total Frequency': total_frequency, 'Websites': websites})

    df = pd.DataFrame(rows)
    df.to_excel(output_excel, index=False)


def read_excel_each_website(input_excel):
    website_words_dict = {}
    df = pd.read_excel(input_excel)

    for _, row in df.iterrows():
        website_url = row['WEB Adress']
        if website_url not in website_words_dict:
            website_words_dict[website_url] = []

        word = row['Most Common Words']
        freq = row['Frequency']
        website_words_dict[website_url].append((word, freq))

    return website_words_dict
