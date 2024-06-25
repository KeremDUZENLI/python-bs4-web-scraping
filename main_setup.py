from mock.mocking import LoadMock

from setup.env import setup_env, setup_output_directory

from tool.tool_csv import create_all_websites_frequent_words_dict_to_csv, create_common_words_among_websites_dict_to_csv, save_websites_status_dict_as_csv
from tool.tool_excel import create_all_websites_frequent_words_dict_to_excel, create_common_words_among_websites_dict_to_excel
from tool.tool_txt import save_frequent_words_dict_as_txt, read_frequent_words_from_txt

from web.web_scrape import create_frequent_words_from_example, create_frequent_words_from_excel


class WebsiteAnalyzer:
    def __init__(self, action_type, output_type, language, xls_type, run_type, top_frequency, http_timeout):
        self.action_type = action_type
        self.output_type = output_type
        self.language = language
        self.xls_type = xls_type
        self.run_type = run_type
        self.top_frequency = top_frequency
        self.http_timeout = http_timeout

        self.deepl_auth_key = setup_env()
        self.target_language_1 = 'DE'
        self.target_language_2 = 'EN-GB'

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

        if self.language in ["DEUTSCH", "BOTH"]:
            create_common_words_among_websites_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_de, self.common_words_among_websites_dict_translated_csv_de)

        if self.language in ["ENGLISH", "BOTH"]:
            create_common_words_among_websites_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_en, self.common_words_among_websites_dict_translated_csv_en)

    def create_common_words_dict_to_xls(self):
        create_common_words_among_websites_dict_to_excel(
            self.all_websites_frequent_words_dict, self.common_words_among_websites_dict_xlsx)

        if self.language in ["DEUTSCH", "BOTH"]:
            create_common_words_among_websites_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_de, self.common_words_among_websites_dict_translated_xlsx_de)

        if self.language in ["ENGLISH", "BOTH"]:
            create_common_words_among_websites_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_en, self.common_words_among_websites_dict_translated_xlsx_en)

    def create_frequent_words_dict_to_csv(self):
        create_all_websites_frequent_words_dict_to_csv(
            self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_csv)

        if self.language in ["DEUTSCH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_csv_de)

        if self.language in ["ENGLISH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_csv(
                self.all_websites_frequent_words_dict_translated_en, self.all_websites_frequent_words_dict_translated_csv_en)

    def create_frequent_words_dict_to_xls(self):
        create_all_websites_frequent_words_dict_to_excel(
            self.all_websites_frequent_words_dict, self.all_websites_frequent_words_dict_xlsx, self.xls_type)

        if self.language in ["DEUTSCH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_de, self.all_websites_frequent_words_dict_translated_xlsx_de, self.xls_type)

        if self.language in ["ENGLISH", "BOTH"]:
            create_all_websites_frequent_words_dict_to_excel(
                self.all_websites_frequent_words_dict_translated_en, self.all_websites_frequent_words_dict_translated_xlsx_en, self.xls_type)


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
        analyzer.all_websites_status_dict_csv = analyzer.directory_output + \
            "all_websites_status.csv"

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
        analyzer.all_websites_frequent_words_dict = []
        analyzer.all_websites_frequent_words_dict_translated_de = []
        analyzer.all_websites_frequent_words_dict_translated_en = []
        analyzer.all_websites_status_dict = {}

        runs_types = {
            None: lambda x: None,

            "MOCK_COMMONS": LoadMock.load_commons_mock,
            "MOCK_FREQUENCY": LoadMock.load_frequency_mock,

            "READ_TXT": read_frequent_words_from_txt,

            "READ_WEBSITES": create_frequent_words_from_example,
            "READ_EXCEL": create_frequent_words_from_excel,
        }

        runs_types.get(analyzer.run_type)(analyzer)
        save_frequent_words_dict_as_txt(analyzer)
        save_websites_status_dict_as_csv(analyzer)
