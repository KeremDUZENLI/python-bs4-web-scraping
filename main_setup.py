from mock.mocking import LoadMock

from setup.env import setup_env, setup_output_directory

from tool.tool_csv import create_all_websites_frequent_words_dict_to_csv, create_common_words_among_websites_dict_to_csv
from tool.tool_excel import create_all_websites_frequent_words_dict_to_excel, create_common_words_among_websites_dict_to_excel
from tool.tool_txt import save_frequent_words_dict_as_txt, read_frequent_words_from_txt

from web.web_scrape import create_frequent_words_from_example, create_frequent_words_from_excel


class WebsiteAnalyzer:
    def __init__(self, top_frequency=5, languages=None, action_type=None, output_type=None, run_type=None):
        self.top_frequency = top_frequency
        self.languages = languages
        self.action_type = action_type
        self.output_type = output_type
        self.run_type = run_type

        xls_version = ["separated", "concatenated"]
        self.xls_version_choice = xls_version[0]

        self.deepl_auth_key = setup_env()
        self.target_language_1 = 'DE'
        self.target_language_2 = 'EN-GB'

        Setup(self.top_frequency,
              self.languages,
              self.action_type,
              self.output_type,
              self.run_type)
        self.create_common_and_frequent_words()

    def create_common_and_frequent_words(self):
        if self.action_type in ["COMMON_WORDS", "BOTH"]:
            self.create_common_words(self)

        if self.action_type in ["FREQUENT_WORDS", "BOTH"]:
            self.create_frequent_words(self)

    def create_common_words(self):
        if self.output_type in ["CSV", "BOTH"]:
            self.create_common_words_dict_to_csv()

        if self.output_type in ["EXCEL", "BOTH"]:
            self.create_common_words_dict_to_xls()

    def create_frequent_words(self):
        if self.output_type in ["CSV", "BOTH"]:
            self.create_frequent_words_dict_to_csv()

        if self.output_type in ["EXCEL", "BOTH"]:
            self.create_frequent_words_dict_to_xls()

    def create_common_words_dict_to_csv(self):
        create_common_words_among_websites_dict_to_csv(
            self.all_websites_frequent_words_dict, self.common_words_among_websites_dict_csv)

        if self.languages in ["DEUTSCH", "BOTH"]:
            create_common_words_among_websites_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_de, self.common_words_among_websites_dict_translated_csv_de)

        if self.languages in ["ENGLISH", "BOTH"]:
            create_common_words_among_websites_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_en, self.common_words_among_websites_dict_translated_csv_en)

    def create_common_words_dict_to_xls(self):
        create_common_words_among_websites_dict_to_excel(
            self.all_websites_frequent_words_dict, self.common_words_among_websites_dict_xlsx)

        if self.languages in ["DEUTSCH", "BOTH"]:
            create_common_words_among_websites_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_de, self.common_words_among_websites_dict_translated_xlsx_de)

        if self.languages in ["ENGLISH", "BOTH"]:
            create_common_words_among_websites_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_en, self.common_words_among_websites_dict_translated_xlsx_en)

    def create_frequent_words_dict_to_csv(self):
        create_all_websites_frequent_words_dict_to_csv(
            self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_csv)

        if self.languages in ["DEUTSCH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_csv_de)

        if self.languages in ["ENGLISH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_en, self.all_websites_frequent_words_dict_translated_csv_en)

    def create_frequent_words_dict_to_xls(self):
        create_all_websites_frequent_words_dict_to_excel(
            self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_xlsx, self.xls_version_choice)

        if self.languages in ["DEUTSCH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_xlsx_de, self.xls_version_choice)

        if self.languages in ["ENGLISH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_en, self.all_websites_frequent_words_dict_translated_xlsx_en, self.xls_version_choice)


class Setup:
    def __init__(self, top_frequency=5, languages=None, action_type=None, output_type=None, run_type=None):
        self.top_frequency = top_frequency
        self.languages = languages
        self.action_type = action_type
        self.output_type = output_type
        self.run_type = run_type

        self.set_input_folders()
        self.set_input_files()
        self.set_output_folders()
        self.set_output_files()
        self.set_dictionaries()

    def set_input_folders(self):
        self.directory_input = "input/"

    def set_input_files(self):
        self.directory_input_excel = self.directory_input + \
            "websites.xlsx"

    def set_output_folders(self):
        self.directory_output = "output/"
        self.directory_output_common_csv = "output/common_words/csv/"
        self.directory_output_common_xls = "output/common_words/xls/"
        self.directory_output_frequent_csv = "output/frequent_words/csv/"
        self.directory_output_frequent_xls = "output/frequent_words/xls/"

        folders = [
            self.directory_output,
            self.directory_output_common_csv,
            self.directory_output_common_xls,
            self.directory_output_frequent_csv,
            self.directory_output_frequent_xls
        ]

        for folder_name in folders:
            setup_output_directory(folder_name)

    def set_output_files(self):
        self.all_websites_frequent_words_dict_txt = self.directory_output + \
            "all_websites_frequent_words_dict.txt"
        self.all_websites_frequent_words_dict_translated_txt_de = self.directory_output + \
            "all_websites_frequent_words_dict_translated_de.txt"
        self.all_websites_frequent_words_dict_translated_txt_en = self.directory_output + \
            "all_websites_frequent_words_dict_translated_en.txt"

        self.common_words_among_websites_dict_csv = self.directory_output_common_csv + \
            "common_words_among_websites_dict.csv"
        self.common_words_among_websites_dict_translated_csv_de = self.directory_output_common_csv + \
            "common_words_among_websites_dict_translated_de.csv"
        self.common_words_among_websites_dict_translated_csv_en = self.directory_output_common_csv + \
            "common_words_among_websites_dict_translated_en.csv"
        self.common_words_among_websites_dict_xlsx = self.directory_output_common_xls + \
            "common_words_among_websites_dict.xlsx"
        self.common_words_among_websites_dict_translated_xlsx_de = self.directory_output_common_xls +\
            "common_words_among_websites_dict_translated_de.xlsx"
        self.common_words_among_websites_dict_translated_xlsx_en = self.directory_output_common_xls +\
            "common_words_among_websites_dict_translated_en.xlsx"

        self.all_websites_frequent_words_dict_csv = self.directory_output_frequent_csv + \
            "all_websites_frequent_words_dict.csv"
        self.all_websites_frequent_words_dict_translated_csv_de = self.directory_output_frequent_csv + \
            "all_websites_frequent_words_dict_translated_de.csv"
        self.all_websites_frequent_words_dict_translated_csv_en = self.directory_output_frequent_csv +\
            "all_websites_frequent_words_dict_translated_en.csv"
        self.all_websites_frequent_words_dict_xlsx = self.directory_output_frequent_xls + \
            "all_websites_frequent_words_dict.xlsx"
        self.all_websites_frequent_words_dict_translated_xlsx_de = self.directory_output_frequent_xls +\
            "all_websites_frequent_words_dict_translated_de.xlsx"
        self.all_websites_frequent_words_dict_translated_xlsx_en = self.directory_output_frequent_xls +\
            "all_websites_frequent_words_dict_translated_en.xlsx"

    def set_dictionaries(self):
        loadMock = LoadMock
        self.all_websites_frequent_words_dict = []
        self.all_websites_frequent_words_dict_translated_de = []
        self.all_websites_frequent_words_dict_translated_en = []
        self.all_websites_url = []

        runs_types = {
            "mock_commons": loadMock.load_commons_mock,
            "mock_frequency": loadMock.load_frequency_mock,

            "read_txt": read_frequent_words_from_txt,

            "read_websites": create_frequent_words_from_example,
            "read_excel": create_frequent_words_from_excel,

            None: lambda x: None
        }

        runs_types.get(self.run_type)(self)
        save_frequent_words_dict_as_txt(self)
