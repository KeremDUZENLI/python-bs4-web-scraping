from collections import defaultdict


def calculate_common_words_tracker(common_words_dict):
    common_words_tracker = defaultdict(set)

    for website_entry in common_words_dict:
        website_url = website_entry['WEB Adress']
        top_words = website_entry['Top Words']

        for word, freq in top_words:
            common_words_tracker[word].add((website_url, freq))

    return common_words_tracker


def sort_common_words(common_words_tracker):
    common_words_between_websites = {
        word: websites for word, websites in common_words_tracker.items() if len(websites) >= 2}
    return sorted(common_words_between_websites.items(), key=lambda x: (len(x[1]), max(x[1], key=lambda y: y[1])[1], x[0]), reverse=True)
