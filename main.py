from input.websites import *

from setup.env import setup_env, setup_output_directory

from tool.tool_csv import create_all_websites_frequent_words_dict_to_csv, create_common_words_among_websites_dict_to_csv
from tool.tool_excel import create_all_websites_frequent_words_dict_to_excel, create_common_words_among_websites_dict_to_excel, read_website_urls_from_excel
from tool.tool_print import print_elements_list, print_elements_dict

from web.web_scrape import create_all_websites_frequent_words_dict
from web.web_translator import create_all_websites_frequent_words_dict_translated


top_frequency = 20
deepl_auth_key = setup_env()
target_language_1 = 'EN-GB'
target_language_2 = 'DE'


all_websites_frequent_words_dict_csv = "all_websites_frequent_words_dict.csv"
all_websites_frequent_words_dict_xlsx = "all_websites_frequent_words_dict.xlsx"
common_words_among_websites_dict_csv = "common_words_among_websites_dict.csv"
common_words_among_websites_dict_xlsx = "common_words_among_websites_dict.xlsx"

all_websites_frequent_words_dict_translated_csv_en = "all_websites_frequent_words_dict_translated_en.csv"
all_websites_frequent_words_dict_translated_xlsx_en = "all_websites_frequent_words_dict_translated_en.xlsx"
common_words_among_websites_dict_translated_csv_en = "common_words_among_websites_dict_translated_en.csv"
common_words_among_websites_dict_translated_xlsx_en = "common_words_among_websites_dict_translated_en.xlsx"

all_websites_frequent_words_dict_translated_csv_de = "all_websites_frequent_words_dict_translated_de.csv"
all_websites_frequent_words_dict_translated_xlsx_de = "all_websites_frequent_words_dict_translated_de.xlsx"
common_words_among_websites_dict_translated_csv_de = "common_words_among_websites_dict_translated_de.csv"
common_words_among_websites_dict_translated_xlsx_de = "common_words_among_websites_dict_translated_de.xlsx"


# website_urls = read_website_urls_from_input_folder
website_urls = read_website_urls_from_excel("input/websites.xlsx")
setup_output_directory("output")


# all_websites_frequent_words_dict = all_websites_frequent_words_dict_example
all_websites_frequent_words_dict = create_all_websites_frequent_words_dict(
    website_urls, top_frequency)
create_all_websites_frequent_words_dict_to_csv(
    all_websites_frequent_words_dict, all_websites_frequent_words_dict_csv)
create_all_websites_frequent_words_dict_to_excel(
    all_websites_frequent_words_dict, all_websites_frequent_words_dict_xlsx, "concatenated")
create_common_words_among_websites_dict_to_csv(
    all_websites_frequent_words_dict, common_words_among_websites_dict_csv)
create_common_words_among_websites_dict_to_excel(
    all_websites_frequent_words_dict, common_words_among_websites_dict_xlsx)


all_websites_frequent_words_dict_translated_en = create_all_websites_frequent_words_dict_translated(
    all_websites_frequent_words_dict, target_language_1, deepl_auth_key)
create_all_websites_frequent_words_dict_to_csv(
    all_websites_frequent_words_dict_translated_en, all_websites_frequent_words_dict_translated_csv_en)
create_all_websites_frequent_words_dict_to_excel(
    all_websites_frequent_words_dict_translated_en, all_websites_frequent_words_dict_translated_xlsx_en)
create_common_words_among_websites_dict_to_csv(
    all_websites_frequent_words_dict_translated_en, common_words_among_websites_dict_translated_csv_en)
create_common_words_among_websites_dict_to_excel(
    all_websites_frequent_words_dict_translated_en, common_words_among_websites_dict_translated_xlsx_en)


all_websites_frequent_words_dict_translated_de = create_all_websites_frequent_words_dict_translated(
    all_websites_frequent_words_dict, target_language_2, deepl_auth_key)
create_all_websites_frequent_words_dict_to_csv(
    all_websites_frequent_words_dict_translated_de, all_websites_frequent_words_dict_translated_csv_de)
create_all_websites_frequent_words_dict_to_excel(
    all_websites_frequent_words_dict_translated_de, all_websites_frequent_words_dict_translated_xlsx_de)
create_common_words_among_websites_dict_to_csv(
    all_websites_frequent_words_dict_translated_de, common_words_among_websites_dict_translated_csv_de)
create_common_words_among_websites_dict_to_excel(
    all_websites_frequent_words_dict_translated_de, common_words_among_websites_dict_translated_xlsx_de)
