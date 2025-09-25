from main_helper import *
from main_setup import WebsiteAnalyzer


def main():
    action_choice = get_type("Select Action Type: ", action_type)
    output_choice = get_type("Select Output Type: ", output_type)
    language_choice = get_type("Select Language: ", language)

    xls_choice = get_type("Select Excel Type: ", xls_type)
    run_choice = get_type("Select Run Type: ", run_type)

    top_frequency = get_input("Enter the top frequency value (default=5): ", 5)
    http_timeout = get_input("Enter the HTTP timeout seconds (default=1): ", 1)

    WebsiteAnalyzer(
        action_type[action_choice],
        output_type[output_choice],
        language[language_choice],

        xls_type[xls_choice],
        run_type[run_choice],

        top_frequency,
        http_timeout
    )

    input("\nProcess completed. Press Enter to exit...")


if __name__ == "__main__":
    main()
