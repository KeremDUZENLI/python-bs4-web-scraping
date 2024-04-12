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

        self.deepl_auth_key = setup_env()
        self.target_language_1 = 'DE'
        self.target_language_2 = 'EN-GB'

        xls_version = ["separated", "concatenated"]
        self.xls_version_choice = xls_version[0]

        Setup(self)
        self.create_common_and_frequent_words()

    def create_common_and_frequent_words(self):
        if self.action_type in ["COMMON_WORDS", "BOTH"]:
            self.create_common_words()

        if self.action_type in ["FREQUENT_WORDS", "BOTH"]:
            self.create_frequent_words()

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
    def __init__(self, analyzer):
        self.set_input_folders(analyzer)
        self.set_input_files(analyzer)
        self.set_output_folders(analyzer)
        self.set_output_files(analyzer)
        self.set_dictionaries(analyzer)

    def set_input_folders(self, analyzer):
        analyzer.directory_input = "input/"

    def set_input_files(self, analyzer):
        analyzer.directory_input_excel = analyzer.directory_input + "websites.xlsx"

    def set_output_folders(self, analyzer):
        analyzer.directory_output = "output/"
        analyzer.directory_output_common_csv = "output/common_words/csv/"
        analyzer.directory_output_common_xls = "output/common_words/xls/"
        analyzer.directory_output_frequent_csv = "output/frequent_words/csv/"
        analyzer.directory_output_frequent_xls = "output/frequent_words/xls/"

        folders = [
            analyzer.directory_output,
            analyzer.directory_output_common_csv,
            analyzer.directory_output_common_xls,
            analyzer.directory_output_frequent_csv,
            analyzer.directory_output_frequent_xls
        ]

        for folder_name in folders:
            setup_output_directory(folder_name)

    def set_output_files(self, analyzer):
        analyzer.all_websites_frequent_words_dict_txt = analyzer.directory_output + \
            "all_websites_frequent_words_dict.txt"
        analyzer.all_websites_frequent_words_dict_translated_txt_de = analyzer.directory_output + \
            "all_websites_frequent_words_dict_translated_de.txt"
        analyzer.all_websites_frequent_words_dict_translated_txt_en = analyzer.directory_output + \
            "all_websites_frequent_words_dict_translated_en.txt"

        analyzer.common_words_among_websites_dict_csv = analyzer.directory_output_common_csv + \
            "common_words_among_websites_dict.csv"
        analyzer.common_words_among_websites_dict_translated_csv_de = analyzer.directory_output_common_csv + \
            "common_words_among_websites_dict_translated_de.csv"
        analyzer.common_words_among_websites_dict_translated_csv_en = analyzer.directory_output_common_csv + \
            "common_words_among_websites_dict_translated_en.csv"
        analyzer.common_words_among_websites_dict_xlsx = analyzer.directory_output_common_xls + \
            "common_words_among_websites_dict.xlsx"
        analyzer.common_words_among_websites_dict_translated_xlsx_de = analyzer.directory_output_common_xls + \
            "common_words_among_websites_dict_translated_de.xlsx"
        analyzer.common_words_among_websites_dict_translated_xlsx_en = analyzer.directory_output_common_xls + \
            "common_words_among_websites_dict_translated_en.xlsx"

        analyzer.all_websites_frequent_words_dict_csv = analyzer.directory_output_frequent_csv + \
            "all_websites_frequent_words_dict.csv"
        analyzer.all_websites_frequent_words_dict_translated_csv_de = analyzer.directory_output_frequent_csv + \
            "all_websites_frequent_words_dict_translated_de.csv"
        analyzer.all_websites_frequent_words_dict_translated_csv_en = analyzer.directory_output_frequent_csv + \
            "all_websites_frequent_words_dict_translated_en.csv"
        analyzer.all_websites_frequent_words_dict_xlsx = analyzer.directory_output_frequent_xls + \
            "all_websites_frequent_words_dict.xlsx"
        analyzer.all_websites_frequent_words_dict_translated_xlsx_de = analyzer.directory_output_frequent_xls + \
            "all_websites_frequent_words_dict_translated_de.xlsx"
        analyzer.all_websites_frequent_words_dict_translated_xlsx_en = analyzer.directory_output_frequent_xls + \
            "all_websites_frequent_words_dict_translated_en.xlsx"

    def set_dictionaries(self, analyzer):
        load_mock = LoadMock
        analyzer.all_websites_frequent_words_dict = []
        analyzer.all_websites_frequent_words_dict_translated_de = []
        analyzer.all_websites_frequent_words_dict_translated_en = []
        analyzer.all_websites_url = []

        runs_types = {
            "mock_commons": load_mock.load_commons_mock,
            "mock_frequency": load_mock.load_frequency_mock,

            "read_txt": read_frequent_words_from_txt,

            "read_websites": create_frequent_words_from_example,
            "read_excel": create_frequent_words_from_excel,

            None: lambda x: None
        }

        runs_types.get(analyzer.run_type)(analyzer)
        save_frequent_words_dict_as_txt(analyzer)
