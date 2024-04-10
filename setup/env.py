import os
from dotenv import load_dotenv

from tool.tool_excel import read_website_urls_from_excel
from web.web_scrape import analyze_websites_translate_create_dict


def setup_env():
    load_dotenv()
    deepl_auth_key = os.getenv('DEEPL_KEY')

    return deepl_auth_key


def setup_output_directory(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    os.chdir(folder_name)


def load_websites_from_excel(class_instance):
    # excel_path = os.path.join(os.path.dirname(
    #     os.path.abspath(__file__)), class_instance.directory_input, "websites.xlsx")

    class_instance.all_websites_url = read_website_urls_from_excel(
        "websites.xlsx")
    analyze_websites_translate_create_dict(class_instance)
