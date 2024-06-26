import requests
from urllib.parse import urlparse
from web.web_tool_helper import clean_html_content, filter_text, get_top_words


def scrape_website_get_frequent_words(website_url, top_frequency, http_timeout, all_websites_status_dict):
    html_content = scrape_website_get_html_content(
        website_url, http_timeout, all_websites_status_dict)
    if html_content is None:
        return {
            'WEB Adress': website_url,
            'Top Words': []}

    website_text = clean_html_content(html_content)
    filtered_text = filter_text(website_text)
    top_words = get_top_words(filtered_text, top_frequency)
    top_words_sorted = sorted(top_words, key=lambda x: (-x[1], x[0]))

    website_common_words_dict = {
        'WEB Adress': website_url,
        'Top Words': top_words_sorted}

    return website_common_words_dict


def scrape_website_get_html_content(website_url, http_timeout, all_websites_status_dict):
    try:
        response = requests.get(website_url, timeout=http_timeout)
        response_time = response.elapsed.total_seconds()

        all_websites_status_dict[website_url] = {
            'status': 'reached',
            'time': response_time}
        print(f"{website_url.ljust(50)} : {response_time:.2f} seconds")

        return response.text

    except Exception as e:
        error_type = type(e).__name__
        all_websites_status_dict[website_url] = {
            'status': 'unreached',
            'error': error_type}
        print(f"{website_url.ljust(50)} : {error_type}")

        return None


def create_unique_website_urls_list(website_urls):
    seen_domains = set()
    unique_website_urls_list = []

    for website_url in website_urls:
        base_domain = extract_base_url(website_url)
        if base_domain not in seen_domains:
            seen_domains.add(base_domain)
            unique_website_urls_list.append("https://" + base_domain)

    return unique_website_urls_list


def extract_base_url(website_url):
    parsed_url = urlparse(website_url)
    base_domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path
    return base_domain.replace('www.', '')
