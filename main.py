import requests
import numpy as np
from PIL import Image
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string
import csv

nltk.download('stopwords')
nltk.download('punkt')

website_urls = [
    "https://www.constantcontact.com/",
    "https://www.interstellarrecords.at/",
    "https://kuprosauwald.org/"
]

csv_file_name = "results.csv"

for website_url in website_urls:
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
        website_text) if word.lower() not in stop_words and not any(char.isdigit() for char in word) and len(word) > 2])

    word_freq = Counter(filtered_text.split())
    top_20_words = word_freq.most_common(20)

    with open(csv_file_name, mode='a', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(['Most Common Words', 'Frequency'])
            writer.writerow([])

        writer.writerow(['Website', website_url])

        for word, freq in top_20_words:
            writer.writerow([word, freq])

        writer.writerow([])
