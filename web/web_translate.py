import deepl


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
