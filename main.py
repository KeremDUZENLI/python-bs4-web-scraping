from setup.directory import setup_output_directory
from setup.env import setup_env
from setup.url_list import setup_list
from tool.csv_tools import create_csv_words_frequency, create_csv_words_translated, create_csv_words_common
from tool.excel_tools import create_excel_words_frequency, create_excel_words_translated, create_excel_words_common


website_urls = [
    "https://www.fuckhead.at/",
    "http://www.interstellarrecords.at/index.php",
    "https://kuprosauwald.org/",
    "https://röda.at/der-verein/",
    "http://www.grgr.at/",
    "https://www.grgr.at/aboutme/",
    "https://qujochoe.org/about/",
    "https://verenamayrhofer.at/",
    "http://hoerstadt.at/uber-uns/",
    "https://www.schlot.info/",
    "https://tinaleisch.at/index.php/tinaleisch/",
    "https://kunstraum.at/en/how-we-are/",
    "https://kunstraum.at/wer-wir-sind/",
    "https://www.kuva.at/",
    "https://jmyyri.com/recliners",
    "https://www.anna-kraher.de/#about"
]
top_frequency = 10
frequent_words_list = setup_list(website_urls, top_frequency)

csv_words_frequency_file = "csv_words_frequency.csv"
csv_words_frequency_translated_en_file = "csv_words_frequency_translated_en.csv"
csv_words_frequency_translated_de_file = "csv_words_frequency_translated_de.csv"
csv_words_common_en_file = "csv_words_common_en.csv"
csv_words_common_de_file = "csv_words_common_de.csv"

excel_words_frequency_file = "excel_words_frequency.xlsx"
excel_words_frequency_translated_en_file = "excel_words_frequency_translated_en.xlsx"
excel_words_frequency_translated_de_file = "excel_words_frequency_translated_de.xlsx"
excel_words_common_en_file = "excel_words_common_en.xlsx"
excel_words_common_de_file = "excel_words_common_de.xlsx"

deepl_auth_key = setup_env()
target_language_1 = 'EN-GB'
target_language_2 = 'DE'


setup_output_directory("output")
create_csv_words_frequency(frequent_words_list, csv_words_frequency_file)
create_excel_words_frequency(frequent_words_list, excel_words_frequency_file)


# create_csv_words_translated(
#     csv_words_frequency_file, csv_words_frequency_translated_en_file, target_language_1, deepl_auth_key)
# create_csv_words_translated(
#     csv_words_frequency_file, csv_words_frequency_translated_de_file, target_language_2, deepl_auth_key)

# create_csv_words_common(
#     csv_words_frequency_translated_en_file, csv_words_common_en_file)
# create_csv_words_common(
#     csv_words_frequency_translated_de_file, csv_words_common_de_file)


# create_excel_words_translated(
#     excel_words_frequency_file, excel_words_frequency_translated_en_file, target_language_1, deepl_auth_key)
# create_excel_words_translated(
#     excel_words_frequency_file, excel_words_frequency_translated_de_file, target_language_2, deepl_auth_key)

create_excel_words_common(
    excel_words_frequency_translated_en_file, excel_words_common_en_file)
create_excel_words_common(
    excel_words_frequency_translated_de_file, excel_words_common_de_file)
