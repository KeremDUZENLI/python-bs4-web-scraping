import requests
from bs4 import BeautifulSoup
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string


nltk.download('stopwords')
nltk.download('punkt')


def scrape_website_get_frequent_words(website_url):
    html_content = requests.get(website_url).text
    website_text = BeautifulSoup(html_content, 'html.parser').get_text()

    delete_text = ["\"", "//", "'", "*", "\n", "\t", "–", "“", "„", "€", "$",
                   "xml version='1.0' encoding='utf-8'?", "html", ""] + list(string.punctuation)
    for text in delete_text:
        website_text = website_text.replace(text, "")

    stop_words_german = set(stopwords.words('german'))
    stop_words_english = set(stopwords.words('english'))
    stop_words = stop_words_german.union(stop_words_english)

    filtered_text = ' '.join([word for word in nltk.word_tokenize(
        website_text) if word.lower() not in stop_words and not any(char.isdigit() for char in word) and len(word) > 2 and len(word) < 30])

    word_freq = Counter(filtered_text.split())
    top_20_words = word_freq.most_common(20)

    common_words_dict = {'WEB Adress': website_url,
                         'Top 20 Words': top_20_words}
    return common_words_dict
