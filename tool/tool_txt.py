import ast


def create_all_websites_frequent_words_dict_to_txt(all_websites_frequent_words_dict, output_txt):
    with open(output_txt, 'w') as f:
        f.write(str(all_websites_frequent_words_dict))


def read_all_websites_frequent_words_dict_from_txt(input_txt):
    with open(input_txt, 'r') as f:
        content = f.read()
        return ast.literal_eval(content)
