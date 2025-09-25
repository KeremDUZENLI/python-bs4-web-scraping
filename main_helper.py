action_type = {0: None,
               1: "BOTH",
               2: "COMMON_WORDS",
               3: "FREQUENT_WORDS"}

output_type = {0: None,
               1: "BOTH",
               2: "CSV",
               3: "EXCEL"}

language = {0: None,
            1: "BOTH",
            2: "DEUTSCH",
            3: "ENGLISH"}

xls_type = {0: None,
            1: "SEPARATE",
            2: "CONCATENATE"}

run_type = {0: None,
            1: "MOCK_COMMONS",
            2: "MOCK_FREQUENCY",
            3: "READ_TXT",
            4: "READ_SAMPLE_WEBSITES",
            5: "READ_EXCEL",
            6: "READ_LLIST"}

top_frequency = 5

http_timeout = 1


def get_type(prompt, choices):
    print("\n" + prompt)
    for key, value in choices.items():
        print(f"{key}: {value}")
    return int(input("Enter your choice: "))


def get_input(prompt, default_value):
    print("\n" + prompt)
    return int(input("Enter your choice: ")) or default_value
