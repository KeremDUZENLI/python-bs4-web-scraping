import ast


def save_frequent_words_dict_as_txt(class_instance):
    create_all_websites_frequent_words_dict_to_txt(
        class_instance.all_websites_frequent_words_dict, class_instance.all_websites_frequent_words_dict_txt)

    if class_instance.language in ["DEUTSCH", "BOTH"]:
        create_all_websites_frequent_words_dict_to_txt(
            class_instance.all_websites_frequent_words_dict_translated_de, class_instance.all_websites_frequent_words_dict_translated_txt_de)

    if class_instance.language in ["ENGLISH", "BOTH"]:
        create_all_websites_frequent_words_dict_to_txt(
            class_instance.all_websites_frequent_words_dict_translated_en, class_instance.all_websites_frequent_words_dict_translated_txt_en)


def read_frequent_words_from_txt(class_instance):
    class_instance.all_websites_frequent_words_dict = read_all_websites_frequent_words_dict_from_txt(
        class_instance.all_websites_frequent_words_dict_txt)

    if class_instance.language in ["DEUTSCH", "BOTH"]:
        class_instance.all_websites_frequent_words_dict_translated_de = read_all_websites_frequent_words_dict_from_txt(
            class_instance.all_websites_frequent_words_dict_translated_txt_de)

    if class_instance.language in ["ENGLISH", "BOTH"]:
        class_instance.all_websites_frequent_words_dict_translated_en = read_all_websites_frequent_words_dict_from_txt(
            class_instance.all_websites_frequent_words_dict_translated_txt_en)


def create_all_websites_frequent_words_dict_to_txt(all_websites_frequent_words_dict, output_txt):
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write(str(all_websites_frequent_words_dict))


def read_all_websites_frequent_words_dict_from_txt(input_txt):
    try:
        with open(input_txt, 'r') as f:
            return ast.literal_eval(f.read())

    except FileNotFoundError:
        return []
