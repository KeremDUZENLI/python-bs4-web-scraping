from main_setup import WebsiteAnalyzer

action_type = ["BOTH", "COMMON_WORDS", "FREQUENT_WORDS"]
output_type = ["BOTH", "CSV", "EXCEL"]
language = ["BOTH", "DEUTSCH", "ENGLISH"]

xls_type = ["SEPARATE", "CONCATENATE"]
run_type = ["MOCK_COMMONS", "MOCK_FREQUENCY",
            "READ_TXT", "READ_WEBSITES", "READ_EXCEL"]

top_frequency = 1


def main():
    WebsiteAnalyzer(
        action_type[0],
        output_type[0],
        language[0],

        xls_type[0],
        run_type[0],

        top_frequency
    )


if __name__ == "__main__":
    main()
