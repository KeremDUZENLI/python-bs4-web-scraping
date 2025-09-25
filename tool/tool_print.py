def print_elements_list(input_list):
    for index, element in enumerate(input_list):
        print(f"{index+1}: {element}")


def print_elements_dict(dictionary_list):
    print('\n\n'.join('\n'.join(f"{key}: {value}" for key, value in website_data.items(
    )) for website_data in dictionary_list))
