from mock.mocking import LoadMock

from setup.env import setup_env, setup_output_directory, my_decorator

from tool.tool_csv import create_all_websites_frequent_words_dict_to_csv, create_common_words_among_websites_dict_to_csv
from tool.tool_excel import create_all_websites_frequent_words_dict_to_excel, create_common_words_among_websites_dict_to_excel
from tool.tool_txt import save_frequent_words_dict_as_txt, read_frequent_words_from_txt

from web.web_scrape import create_frequent_words_from_example, create_frequent_words_from_excel


class WebsiteAnalyzer:
    directory_frequent = "frequent_words"
    directory_common = "common_words"
    directory_csv = "csv"
    directory_xls = "excel"

    def __init__(self, top_frequency=5, languages=None, output_type=None, act=None):
        self.top_frequency = top_frequency
        self.languages = languages
        self.output_type = output_type
        self.act = act

        xls_version = ["seperated", "concatenated"]
        self.xls_version_choice = xls_version[0]

        self.deepl_auth_key = setup_env()
        self.directory_input = "input"
        self.directory_output = "output"
        self.target_language_1 = 'DE'
        self.target_language_2 = 'EN-GB'

        setup = Setup
        setup.set_output_files(self)
        setup.set_dictionaries(self, act)

    @my_decorator(directory_frequent)
    def create_frequent_words(self):
        if self.output_type in ["CSV", "BOTH"]:
            self.create_frequent_words_dict_to_csv()

        if self.output_type in ["EXCEL", "BOTH"]:
            self.create_frequent_words_dict_to_xls()

    @my_decorator(directory_common)
    def create_common_words(self):
        if self.output_type in ["CSV", "BOTH"]:
            self.create_common_words_dict_to_csv()

        if self.output_type in ["EXCEL", "BOTH"]:
            self.create_common_words_dict_to_xls()

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
    def create_frequent_words_dict_to_xls(self):
        create_all_websites_frequent_words_dict_to_excel(
            self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_xlsx, self.xls_version_choice)

        if self.languages in ["DEUTSCH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_xlsx_de, self.xls_version_choice)

        if self.languages in ["ENGLISH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_en, self.all_websites_frequent_words_dict_translated_xlsx_en, self.xls_version_choice)

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


class Setup:
    def set_output_files(class_instance):
        setup_output_directory(class_instance.directory_output)
        class_instance.all_websites_frequent_words_dict_txt = "all_websites_frequent_words_dict.txt"
        class_instance.all_websites_frequent_words_dict_translated_txt_de = "all_websites_frequent_words_dict_translated_de.txt"
        class_instance.all_websites_frequent_words_dict_translated_txt_en = "all_websites_frequent_words_dict_translated_en.txt"

        class_instance.all_websites_frequent_words_dict_csv = "all_websites_frequent_words_dict.csv"
        class_instance.all_websites_frequent_words_dict_xlsx = "all_websites_frequent_words_dict.xlsx"
        class_instance.all_websites_frequent_words_dict_translated_csv_de = "all_websites_frequent_words_dict_translated_de.csv"
        class_instance.all_websites_frequent_words_dict_translated_xlsx_de = "all_websites_frequent_words_dict_translated_de.xlsx"
        class_instance.all_websites_frequent_words_dict_translated_csv_en = "all_websites_frequent_words_dict_translated_en.csv"
        class_instance.all_websites_frequent_words_dict_translated_xlsx_en = "all_websites_frequent_words_dict_translated_en.xlsx"

        class_instance.common_words_among_websites_dict_csv = "common_words_among_websites_dict.csv"
        class_instance.common_words_among_websites_dict_xlsx = "common_words_among_websites_dict.xlsx"
        class_instance.common_words_among_websites_dict_translated_csv_de = "common_words_among_websites_dict_translated_de.csv"
        class_instance.common_words_among_websites_dict_translated_xlsx_de = "common_words_among_websites_dict_translated_de.xlsx"
        class_instance.common_words_among_websites_dict_translated_csv_en = "common_words_among_websites_dict_translated_en.csv"
        class_instance.common_words_among_websites_dict_translated_xlsx_en = "common_words_among_websites_dict_translated_en.xlsx"

    def set_dictionaries(class_instance, act=None):
        loadMock = LoadMock
        class_instance.all_websites_frequent_words_dict = []
        class_instance.all_websites_frequent_words_dict_translated_de = []
        class_instance.all_websites_frequent_words_dict_translated_en = []
        class_instance.all_websites_url = []

        actions = {
            "mock_commons": loadMock.load_commons_mock,
            "mock_frequency": loadMock.load_frequency_mock,

            "read_txt": read_frequent_words_from_txt,

            "mock_websites": create_frequent_words_from_example,
            "read_excel": create_frequent_words_from_excel,

            None: lambda x: None
        }

        actions.get(act)(class_instance)
        save_frequent_words_dict_as_txt(class_instance)
