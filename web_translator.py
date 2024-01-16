import deepl


def words_translate_deepl(text, target_language, deepl_auth_key):
    translator = deepl.Translator(deepl_auth_key)
    return translator.translate_text(text, target_lang=target_language)
