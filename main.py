import os
from input.websites import *

from setup.env import setup_env, setup_output_directory

from tool.tool_csv import create_all_websites_frequent_words_dict_to_csv, create_common_words_among_websites_dict_to_csv
from tool.tool_excel import create_all_websites_frequent_words_dict_to_excel, create_common_words_among_websites_dict_to_excel, read_website_urls_from_excel
from tool.tool_print import print_elements_list, print_elements_dict
from tool.tool_txt import create_all_websites_frequent_words_dict_to_txt, read_all_websites_frequent_words_dict_from_txt

from web.web_scrape import create_all_websites_frequent_words_dict
from web.web_translator import create_all_websites_frequent_words_dict_translated


def my_decorator(folder_name):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            setup_output_directory(folder_name)
            func(self, *args, **kwargs)
            os.chdir("../")
        return wrapper
    return decorator


class WebsiteAnalyzer:
    directory_out = "output"
    directory_frequent = "frequent_words"
    directory_common = "common_words"
    directory_csv = "csv"
    directory_xls = "excel"

    def __init__(self, top_frequency=5, languages=None, output_type=None):
        self.top_frequency = top_frequency
        self.languages = languages
        self.output_type = output_type

        xls_version = ["seperated", "concatenated"]
        self.xls_version_choice = xls_version[0]

        self.deepl_auth_key = setup_env()
        self.target_language_1 = 'DE'
        self.target_language_2 = 'EN-GB'

        self.set_output_files()
        self.set_dictionaries("mock_websites")

    def set_output_files(self):
        setup_output_directory(self.directory_out)

        self.all_websites_frequent_words_dict_txt = "all_websites_frequent_words_dict.txt"
        self.all_websites_frequent_words_dict_translated_txt_de = "all_websites_frequent_words_dict_translated_de.txt"
        self.all_websites_frequent_words_dict_translated_txt_en = "all_websites_frequent_words_dict_translated_en.txt"

        self.all_websites_frequent_words_dict_csv = "all_websites_frequent_words_dict.csv"
        self.all_websites_frequent_words_dict_xlsx = "all_websites_frequent_words_dict.xlsx"
        self.all_websites_frequent_words_dict_translated_csv_de = "all_websites_frequent_words_dict_translated_de.csv"
        self.all_websites_frequent_words_dict_translated_xlsx_de = "all_websites_frequent_words_dict_translated_de.xlsx"
        self.all_websites_frequent_words_dict_translated_csv_en = "all_websites_frequent_words_dict_translated_en.csv"
        self.all_websites_frequent_words_dict_translated_xlsx_en = "all_websites_frequent_words_dict_translated_en.xlsx"

        self.common_words_among_websites_dict_csv = "common_words_among_websites_dict.csv"
        self.common_words_among_websites_dict_xlsx = "common_words_among_websites_dict.xlsx"
        self.common_words_among_websites_dict_translated_csv_de = "common_words_among_websites_dict_translated_de.csv"
        self.common_words_among_websites_dict_translated_xlsx_de = "common_words_among_websites_dict_translated_de.xlsx"
        self.common_words_among_websites_dict_translated_csv_en = "common_words_among_websites_dict_translated_en.csv"
        self.common_words_among_websites_dict_translated_xlsx_en = "common_words_among_websites_dict_translated_en.xlsx"

    def set_dictionaries(self, mock=None):
        self.all_websites_frequent_words_dict = []
        self.all_websites_frequent_words_dict_translated_de = []
        self.all_websites_frequent_words_dict_translated_en = []
        self.all_websites_url = []

        if mock == "mock_frequency":
            self.all_websites_frequent_words_dict = all_websites_frequent_words_dict_example
            self.all_websites_frequent_words_dict_translated_de = all_websites_frequent_words_dict_translated_de_example
            self.all_websites_frequent_words_dict_translated_en = all_websites_frequent_words_dict_translated_en_example

        if mock == "mock_commons":
            self.all_websites_frequent_words_dict = common_words_among_websites_dict_example
            self.all_websites_frequent_words_dict_translated_de = common_words_among_websites_dict_translated_de_example
            self.all_websites_frequent_words_dict_translated_en = common_words_among_websites_dict_translated_en_example

        if mock == "mock_txt":
            self.read_frequent_words_from_txt()

        if mock == "mock_websites":
            self.all_websites_url = read_website_urls_from_example
            self.analyze_websites_translate_create_dict()

        else:
            self.all_websites_url = read_website_urls_from_excel(
                "input/websites.xlsx")
            self.analyze_websites_translate_create_dict()

        self.save_frequent_words_dict_as_txt()

    def analyze_websites_translate_create_dict(self):
        self.all_websites_frequent_words_dict = create_all_websites_frequent_words_dict(
            self.all_websites_url, self.top_frequency)

        if self.languages in ["DEUTSCH", "BOTH"]:
            self.all_websites_frequent_words_dict_translated_de = create_all_websites_frequent_words_dict_translated(
                self.all_websites_frequent_words_dict, self.target_language_1, self.deepl_auth_key)

        if self.languages in ["ENGLISH", "BOTH"]:
            self.all_websites_frequent_words_dict_translated_en = create_all_websites_frequent_words_dict_translated(
                self.all_websites_frequent_words_dict, self.target_language_2, self.deepl_auth_key)

    def save_frequent_words_dict_as_txt(self):
        create_all_websites_frequent_words_dict_to_txt(
            self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_txt)

        if self.languages in ["DEUTSCH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_txt(
                self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_txt_de)

        if self.languages in ["ENGLISH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_txt(
                self.all_websites_frequent_words_dict_translated_en, self.all_websites_frequent_words_dict_translated_txt_en)

    def read_frequent_words_from_txt(self):
        self.all_websites_frequent_words_dict = read_all_websites_frequent_words_dict_from_txt(
            self.all_websites_frequent_words_dict_txt)

        if self.languages in ["DEUTSCH", "BOTH"]:
            self.all_websites_frequent_words_dict_translated_de = read_all_websites_frequent_words_dict_from_txt(
                self.all_websites_frequent_words_dict_translated_txt_de)

        if self.languages in ["ENGLISH", "BOTH"]:
            self.all_websites_frequent_words_dict_translated_en = read_all_websites_frequent_words_dict_from_txt(
                self.all_websites_frequent_words_dict_translated_txt_en)

    @my_decorator(directory_frequent)
    def create_frequent_words(self):
        if self.output_type in ["CSV", "BOTH"]:
            self.create_frequent_words_dict_to_csv()

        if self.output_type in ["EXCEL", "BOTH"]:
            self.create_frequent_words_dict_to_xls()

    @my_decorator(directory_csv)
    def create_frequent_words_dict_to_csv(self):
        create_all_websites_frequent_words_dict_to_csv(
            self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_csv)

        if self.languages in ["DEUTSCH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_csv_de)

        if self.languages in ["ENGLISH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_en, self.all_websites_frequent_words_dict_translated_csv_en)

    @my_decorator(directory_xls)
    def create_frequent_words_dict_to_xls(self):
        create_all_websites_frequent_words_dict_to_excel(
            self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_xlsx, self.xls_version_choice)

        if self.languages in ["DEUTSCH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_xlsx_de, self.xls_version_choice)

        if self.languages in ["ENGLISH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_en, self.all_websites_frequent_words_dict_translated_xlsx_en, self.xls_version_choice)

    @my_decorator(directory_common)
    def create_common_words(self):
        if self.output_type in ["CSV", "BOTH"]:
            self.create_common_words_dict_to_csv()

        if self.output_type in ["EXCEL", "BOTH"]:
            self.create_common_words_dict_to_xls()

    @my_decorator(directory_csv)
    def create_common_words_dict_to_csv(self):
        create_common_words_among_websites_dict_to_csv(
            self.all_websites_frequent_words_dict, self.common_words_among_websites_dict_csv)

        if self.languages in ["DEUTSCH", "BOTH"]:
            create_common_words_among_websites_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_de, self.common_words_among_websites_dict_translated_csv_de)

        if self.languages in ["ENGLISH", "BOTH"]:
            create_common_words_among_websites_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_en, self.common_words_among_websites_dict_translated_csv_en)

    @my_decorator(directory_xls)
    def create_common_words_dict_to_xls(self):
        create_common_words_among_websites_dict_to_excel(
            self.all_websites_frequent_words_dict, self.common_words_among_websites_dict_xlsx)

        if self.languages in ["DEUTSCH", "BOTH"]:
            create_common_words_among_websites_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_de, self.common_words_among_websites_dict_translated_xlsx_de)

        if self.languages in ["ENGLISH", "BOTH"]:
            create_common_words_among_websites_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_en, self.common_words_among_websites_dict_translated_xlsx_en)


analyzer = WebsiteAnalyzer(3, "BOTH", "BOTH")
analyzer.create_frequent_words()
analyzer.create_common_words()
