def save_websites_clean_dict_as_llist(class_instance):
    create_websites_clean_llist(
        class_instance.all_websites_status_dict, class_instance.all_websites_clean_dict_llist)


def create_websites_clean_llist(websites_dict, output_llist):
    with open(output_llist, 'w') as file:
        for website_url in websites_dict.keys():
            file.write(website_url + '\n')


def read_websites_from_llist(input_llist):
    try:
        with open(input_llist, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
