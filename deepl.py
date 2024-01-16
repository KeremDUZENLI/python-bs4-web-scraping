import os
import deepl
from dotenv import load_dotenv

load_dotenv()


def translate_with_deepl(text, target_language, deepl_auth_key):
    translator = deepl.Translator(deepl_auth_key)
    return translator.translate_text(text, target_lang=target_language)


text = 'Wie alt bist du'
target_language = 'EN-GB'
deepl_auth_key = os.getenv('DEEPL_KEY')


if deepl_auth_key:
    print(translate_with_deepl(text, target_language, deepl_auth_key))
else:
    print("DeepL API key not found. Please set the DEEPL_KEY environment variable in your .env file.")
