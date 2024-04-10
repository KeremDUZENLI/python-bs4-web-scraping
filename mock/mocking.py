from tool.tool_txt import read_frequent_words_from_txt
from web.web_scrape import analyze_websites_translate_create_dict

from mock.mock_common import common_words_among_websites_dict_example, common_words_among_websites_dict_translated_de_example, common_words_among_websites_dict_translated_en_example
from mock.mock_frequent import all_websites_frequent_words_dict_example, all_websites_frequent_words_dict_translated_de_example, all_websites_frequent_words_dict_translated_en_example
from mock.mock_website import read_website_urls_from_example


class LoadMock:
    @staticmethod
    def load_commons_mock(class_instance):
        class_instance.all_websites_frequent_words_dict = common_words_among_websites_dict_example
        class_instance.all_websites_frequent_words_dict_translated_de = common_words_among_websites_dict_translated_de_example
        class_instance.all_websites_frequent_words_dict_translated_en = common_words_among_websites_dict_translated_en_example

    @staticmethod
    def load_frequency_mock(class_instance):
        class_instance.all_websites_frequent_words_dict = all_websites_frequent_words_dict_example
        class_instance.all_websites_frequent_words_dict_translated_de = all_websites_frequent_words_dict_translated_de_example
        class_instance.all_websites_frequent_words_dict_translated_en = all_websites_frequent_words_dict_translated_en_example

    @staticmethod
    def load_websites_mock(class_instance):
        class_instance.all_websites_url = read_website_urls_from_example
        analyze_websites_translate_create_dict(class_instance)
