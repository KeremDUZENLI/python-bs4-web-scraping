import os
from dotenv import load_dotenv


def setup_env():
    load_dotenv()
    deepl_auth_key = os.getenv('DEEPL_KEY')

    return deepl_auth_key
