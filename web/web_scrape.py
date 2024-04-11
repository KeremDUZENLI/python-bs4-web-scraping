from web.web_tool import scrape_website_get_frequent_words
from web.web_translate import translate_top_words

from input.websites import website_urls_example
from tool.tool_excel import read_website_urls_from_excel


def create_frequent_words_from_example(class_instance):
    class_instance.all_websites_url = website_urls_example
    analyze_websites_translate_create_dict(class_instance)


def create_frequent_words_from_excel(class_instance):
    class_instance.all_websites_url = read_website_urls_from_excel(
        class_instance.directory_input_excel)
    analyze_websites_translate_create_dict(class_instance)


def analyze_websites_translate_create_dict(class_instance):
    class_instance.all_websites_frequent_words_dict = create_all_websites_frequent_words_dict(
        class_instance.all_websites_url, class_instance.top_frequency)

    if class_instance.languages in ["DEUTSCH", "BOTH"]:
        class_instance.all_websites_frequent_words_dict_translated_de = create_all_websites_frequent_words_dict_translated(
            class_instance.all_websites_frequent_words_dict, class_instance.target_language_1, class_instance.deepl_auth_key)

    if class_instance.languages in ["ENGLISH", "BOTH"]:
        class_instance.all_websites_frequent_words_dict_translated_en = create_all_websites_frequent_words_dict_translated(
            class_instance.all_websites_frequent_words_dict, class_instance.target_language_2, class_instance.deepl_auth_key)


def create_all_websites_frequent_words_dict(website_urls, top_frequency):
    all_websites_frequent_words_dict = []

    for website_url in website_urls:
        website_common_words_dict = scrape_website_get_frequent_words(
            website_url, top_frequency)

        if website_common_words_dict is None:
            website_common_words_dict = {'WEB Adress': website_url,
                                         'Top Words': None}
        all_websites_frequent_words_dict.append(website_common_words_dict)

    return all_websites_frequent_words_dict


def create_all_websites_frequent_words_dict_translated(all_websites_frequent_words_dict, target_language, deepl_auth_key):
    all_websites_frequent_words_dict_translated = []

    for website_common_words_dict in all_websites_frequent_words_dict:
        website_url = website_common_words_dict['WEB Adress']
        top_words = website_common_words_dict['Top Words']

        translated_top_words = translate_top_words(
            top_words, target_language, deepl_auth_key)
        translated_top_words_sorted = sorted(
            translated_top_words, key=lambda x: (-x[1], x[0]))

        all_websites_frequent_words_dict_translated.append(
            {'WEB Adress': website_url,
             'Top Words': translated_top_words_sorted})

    return all_websites_frequent_words_dict_translated
