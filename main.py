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
    directory_txt = "txt"
    directory_csv = "csv"
    directory_xls = "excel"
    directory_common = "common_words"

    def __init__(self, top_frequency=5):
        self.top_frequency = top_frequency
        self.deepl_auth_key = setup_env()

        self.target_language_1 = 'DE'
        self.target_language_2 = 'EN-GB'

        self.set_dictionaries("websites", "EN")
        self.set_output_files()

    def set_dictionaries(self, mock=None, language=None):
        self.all_websites_frequent_words_dict = []
        self.all_websites_frequent_words_dict_translated_de = []
        self.all_websites_frequent_words_dict_translated_en = []
        self.website_urls = read_website_urls_from_excel("input/websites.xlsx")

        if mock == "frequency":
            self.all_websites_frequent_words_dict = all_websites_frequent_words_dict_example
            self.all_websites_frequent_words_dict_translated_de = all_websites_frequent_words_dict_translated_de_example
            self.all_websites_frequent_words_dict_translated_en = all_websites_frequent_words_dict_translated_en_example
            return

        if mock == "commons":
            self.all_websites_frequent_words_dict = common_words_among_websites_dict_example
            self.all_websites_frequent_words_dict_translated_de = common_words_among_websites_dict_translated_de_example
            self.all_websites_frequent_words_dict_translated_en = common_words_among_websites_dict_translated_en_example
            return

        if mock == "websites":
            self.website_urls = read_website_urls_from_example

        return self.analyze_websites_translate_create_dict(language)

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

    def analyze_websites_translate_create_dict(self, language=None):
        self.all_websites_frequent_words_dict = create_all_websites_frequent_words_dict(
            self.website_urls, self.top_frequency)

        if language in ["DE", "BOTH"]:
            self.all_websites_frequent_words_dict_translated_de = create_all_websites_frequent_words_dict_translated(
                self.all_websites_frequent_words_dict, self.target_language_1, self.deepl_auth_key)

        if language in ["EN", "BOTH"]:
            self.all_websites_frequent_words_dict_translated_en = create_all_websites_frequent_words_dict_translated(
                self.all_websites_frequent_words_dict, self.target_language_2, self.deepl_auth_key)

        return self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_en

    @my_decorator(directory_txt)
    def create_frequent_words_dict_to_txt(self):
        create_all_websites_frequent_words_dict_to_txt(
            self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_txt)
        create_all_websites_frequent_words_dict_to_txt(
            self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_txt_de)
        create_all_websites_frequent_words_dict_to_txt(
            self.all_websites_frequent_words_dict_translated_en, self.all_websites_frequent_words_dict_translated_txt_en)

    @my_decorator(directory_txt)
    def read_frequent_words_from_txt(self):
        self.all_websites_frequent_words_dict = read_all_websites_frequent_words_dict_from_txt(
            self.all_websites_frequent_words_dict_txt)
        self.all_websites_frequent_words_dict_translated_de = read_all_websites_frequent_words_dict_from_txt(
            self.all_websites_frequent_words_dict_translated_txt_de)
        self.all_websites_frequent_words_dict_translated_en = read_all_websites_frequent_words_dict_from_txt(
            self.all_websites_frequent_words_dict_translated_txt_en)

    @my_decorator(directory_csv)
    def create_dict_to_csv(self, language=None):
        create_all_websites_frequent_words_dict_to_csv(
            self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_csv)

        if language in ["DE", "BOTH"]:
            create_all_websites_frequent_words_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_csv_de)

        if language in ["EN", "BOTH"]:
            create_all_websites_frequent_words_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_en, self.all_websites_frequent_words_dict_translated_csv_en)

    @my_decorator(directory_xls)
    def create_dict_to_excel(self, language=None, version="seperated"):
        create_all_websites_frequent_words_dict_to_excel(
            self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_xlsx, version)

        if language in ["DE", "BOTH"]:
            create_all_websites_frequent_words_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_xlsx_de, version)

        if language in ["EN", "BOTH"]:
            create_all_websites_frequent_words_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_en, self.all_websites_frequent_words_dict_translated_xlsx_en, version)

    @my_decorator(directory_common)
    def create_common_words_among_websites(self, output_type="BOTH"):
        if output_type in ["CSV", "BOTH"]:
            create_common_words_among_websites_dict_to_csv(
                self.all_websites_frequent_words_dict, self.common_words_among_websites_dict_csv)
            create_common_words_among_websites_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_de, self.common_words_among_websites_dict_translated_csv_de)
            create_common_words_among_websites_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_en, self.common_words_among_websites_dict_translated_csv_en)

        if output_type in ["EXCEL", "BOTH"]:
            create_common_words_among_websites_dict_to_excel(
                self.all_websites_frequent_words_dict, self.common_words_among_websites_dict_xlsx)
            create_common_words_among_websites_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_de, self.common_words_among_websites_dict_translated_xlsx_de)
            create_common_words_among_websites_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_en, self.common_words_among_websites_dict_translated_xlsx_en)


analyzer = WebsiteAnalyzer(2)

analyzer.create_frequent_words_dict_to_txt()
# analyzer.read_frequent_words_from_txt()

# analyzer.create_dict_to_csv("BOTH")
# analyzer.create_dict_to_excel("BOTH")

# analyzer.create_common_words_among_websites("CSV")
