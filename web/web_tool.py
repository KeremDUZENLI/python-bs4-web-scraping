import string
import requests
import nltk
from nltk.corpus import stopwords
from collections import Counter
from bs4 import BeautifulSoup


nltk.download('stopwords')
nltk.download('punkt')


STOP_WORDS_GERMAN = set(stopwords.words('german'))
STOP_WORDS_ENGLISH = set(stopwords.words('english'))
DELETE_TEXT = ["\"", "//", "'", "*", "\n", "\t", "–", "“", "„", "€", "$",
               "xml version='1.0' encoding='utf-8'?", "html", ""] + list(string.punctuation)


def scrape_website_get_frequent_words(website_url, top_frequency, http_timeout, unreached_websites_dict):
    html_content = scrape_website_get_html_content(
        website_url, http_timeout, unreached_websites_dict)
    if html_content is None:
        return {
            'WEB Adress': website_url,
            'Top Words': []}

    website_text = clean_html_content(html_content)
    filtered_text = filter_text(website_text)
    top_words = get_top_words(filtered_text, top_frequency)
    top_words_sorted = sorted(top_words, key=lambda x: (-x[1], x[0]))

    website_common_words_dict = {
        'WEB Adress': website_url,
        'Top Words': top_words_sorted}

    return website_common_words_dict


def scrape_website_get_html_content(website_url, http_timeout, unreached_websites_dict):
    try:
        return requests.get(website_url, timeout=http_timeout).text

    except Exception as e:
        error_type = type(e).__name__
        unreached_websites_dict.append((website_url, error_type))
        print(f"{website_url.ljust(30)} : {error_type}")

        return None


def clean_html_content(html_content):
    if html_content is None:
        return None

    soup = BeautifulSoup(html_content, 'html.parser')
    website_text = soup.get_text()

    for text in DELETE_TEXT:
        website_text = website_text.replace(text, "")

    return website_text


def filter_text(website_text):
    if website_text is None:
        return None

    stop_words = STOP_WORDS_GERMAN.union(STOP_WORDS_ENGLISH)

    tokenized_words = nltk.word_tokenize(website_text)
    filtered_words = [word.capitalize() for word in tokenized_words
                      if word.lower() not in stop_words
                      and not any(char.isdigit() for char in word)
                      and 2 < len(word) < 30]

    cleaned_words = [word.strip(string.punctuation) for word in filtered_words]
    filtered_text = ' '.join(cleaned_words)

    return filtered_text


def get_top_words(filtered_text, top_frequency):
    if filtered_text is None:
        return None

    word_freq = Counter(filtered_text.split())
    filtered_freq = {word: freq for word,
                     freq in word_freq.items() if freq > 1}
    top_words = Counter(filtered_freq).most_common(top_frequency)

    return top_words
