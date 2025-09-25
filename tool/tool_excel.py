import pandas as pd
from tool.tool import calculate_common_words_tracker, sort_common_words


def create_all_websites_frequent_words_dict_to_excel(all_websites_frequent_words_dict, output_excel, xls_type):
    if not all_websites_frequent_words_dict or xls_type == None:
        empty_df = pd.DataFrame(
            columns=['WEB Adress', 'Most Frequent Words', 'Frequency'])
        empty_df.to_excel(output_excel, index=False)
        return

    dfs = []

    if xls_type == "SEPARATE":
        create_website_df = create_website_df_seperated
        columns = ['WEB Adress', 'Most Frequent Words', 'Frequency']

    if xls_type == "CONCATENATE":
        create_website_df = create_website_df_concatenated
        columns = ['WEB Adress', 'Most Frequent Words']

    for website_frequent_words_dict in all_websites_frequent_words_dict:
        website_url = website_frequent_words_dict['WEB Adress']
        top_words_and_frequency = website_frequent_words_dict['Top Words']
        website_df = create_website_df(website_url, top_words_and_frequency)
        dfs.append(website_df)

    df = pd.concat(dfs, ignore_index=True)
    df = df[columns]
    df.to_excel(output_excel, index=False)


def create_common_words_among_websites_dict_to_excel(all_websites_frequent_words_dict, output_excel):
    common_words_tracker = calculate_common_words_tracker(
        all_websites_frequent_words_dict)
    sorted_common_words = sort_common_words(common_words_tracker)
    write_sorted_common_words_to_excel(output_excel, sorted_common_words)


def write_sorted_common_words_to_excel(output_excel, sorted_common_words):
    rows = []
    for word, websites_freq in sorted_common_words:
        websites = ', '.join(
            sorted([f"{site} ({freq})" for site, freq in websites_freq]))
        total_frequency = sum(freq for _, freq in websites_freq)
        rows.append(
            {'Common Word': word, 'Total Frequency': total_frequency, 'Websites': websites})

    df = pd.DataFrame(rows)
    df.to_excel(output_excel, index=False)


def create_website_df_seperated(website_url, top_words_and_frequency):
    if not top_words_and_frequency:
        return pd.DataFrame(
            {'WEB Adress': [website_url], 'Most Frequent Words': [''], 'Frequency': ['']})
    else:
        website_df = pd.DataFrame(top_words_and_frequency, columns=[
                                  'Most Frequent Words', 'Frequency'])
        website_df['WEB Adress'] = website_url
        return pd.concat(
            [website_df, pd.DataFrame([{}], columns=website_df.columns)], ignore_index=True)


def create_website_df_concatenated(website_url, top_words_and_frequency, freq_value=False):
    if not top_words_and_frequency:
        return pd.DataFrame(
            {'WEB Adress': [website_url], 'Most Frequent Words': ['']})
    else:
        if freq_value:
            words = '; '.join(
                [f'{word} ({freq})' for word, freq in top_words_and_frequency])
        else:
            words = '; '.join(
                [word for word, _ in top_words_and_frequency])

        return pd.DataFrame(
            {'WEB Adress': [website_url], 'Most Frequent Words': [words]})


def read_website_urls_from_excel(input_excel):
    try:
        df = pd.read_excel(input_excel)
        return ['http://' + url for url in df['Websites'].unique().tolist()]
    except FileNotFoundError:
        return []
