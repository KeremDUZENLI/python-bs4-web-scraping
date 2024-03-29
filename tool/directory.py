import os
from dotenv import load_dotenv


def setup_directory_csv(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    os.chdir(folder_name)


def setup_env():
    load_dotenv()
    deepl_auth_key = os.getenv('DEEPL_KEY')
    return deepl_auth_key
