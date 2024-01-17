from tool.directory import setup_directory_csv, setup_env
from web.web_scrape import scrape_website_get_frequent_words
from tool.csv_tools import create_csv_words_frequency, create_csv_words_translated, create_csv_words_common, read_csv_each_website


setup_directory_csv("csv")
deepl_auth_key = setup_env()

target_language_1 = 'EN-GB'
target_language_2 = 'DE'

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

frequent_words_list = []

for url in website_urls:
    words_dict = scrape_website_get_frequent_words(url)
    frequent_words_list.append(words_dict)

create_csv_words_frequency(frequent_words_list, "csv_words_frequency.csv")


create_csv_words_translated(
    "csv_words_frequency.csv", "csv_words_frequency_translated_en.csv", target_language_1, deepl_auth_key)
create_csv_words_translated(
    "csv_words_frequency.csv", "csv_words_frequency_translated_de.csv", target_language_2, deepl_auth_key)
create_csv_words_common(
    "csv_words_frequency_translated_en.csv", "csv_words_common_en.csv")
create_csv_words_common(
    "csv_words_frequency_translated_de.csv", "csv_words_common_de.csv")
