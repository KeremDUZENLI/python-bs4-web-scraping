import os
from dotenv import load_dotenv


def setup_env():
    load_dotenv()
    deepl_auth_key = os.getenv('DEEPL_KEY')

    return deepl_auth_key


def setup_output_directory(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    os.chdir(folder_name)


def my_decorator(folder_name):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            setup_output_directory(folder_name)
            func(self, *args, **kwargs)
            os.chdir("../")
        return wrapper
    return decorator
