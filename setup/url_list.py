from web.web_scrape import scrape_website_get_frequent_words


def setup_list(website_urls, top_frequency):
    frequent_words_list = []

    for url in website_urls:
        words_dict = scrape_website_get_frequent_words(url, top_frequency)
        frequent_words_list.append(words_dict)

    return frequent_words_list
