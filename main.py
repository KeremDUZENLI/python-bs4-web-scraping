from main_setup import WebsiteAnalyzer

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
            4: "READ_WEBSITES",
            5: "READ_EXCEL"}

top_frequency = 10


def main():
    WebsiteAnalyzer(
        action_type[1],
        output_type[3],
        language[0],

        xls_type[1],
        run_type[5],

        top_frequency
    )


if __name__ == "__main__":
    main()
