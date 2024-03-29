import deepl


def create_all_websites_frequent_words_dict_translated(all_websites_frequent_words_dict, target_language, deepl_auth_key):
    all_websites_frequent_words_dict_translated = []

    for website_common_words_dict in all_websites_frequent_words_dict:
        website_url = website_common_words_dict['WEB Adress']
        top_words = website_common_words_dict['Top Words']

        translated_top_words = translate_top_words(
            top_words, target_language, deepl_auth_key)
        translated_top_words_sorted = sorted(
            translated_top_words, key=lambda x: (-x[1], x[0]))

        all_websites_frequent_words_dict_translated.append(
            {'WEB Adress': website_url,
             'Top Words': translated_top_words_sorted})

    return all_websites_frequent_words_dict_translated


def translate_top_words(top_words, target_language, deepl_auth_key):
    translated_top_words = []

    for word, freq in top_words:
        translated_word = word_translate_deepl(
            word, target_language, deepl_auth_key).capitalize()
        translated_top_words.append((translated_word, freq))

    return translated_top_words


def word_translate_deepl(word, target_language, deepl_auth_key):
    translator = deepl.Translator(deepl_auth_key)
    return translator.translate_text(word, target_lang=target_language).text
