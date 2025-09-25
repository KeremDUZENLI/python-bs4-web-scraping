import string
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
