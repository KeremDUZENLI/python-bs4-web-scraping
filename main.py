from main_setup import WebsiteAnalyzer


def main():
    analyzer = WebsiteAnalyzer(
        top_frequency=1, languages="BOTH", output_type="BOTH", action_type="read_excel")

    analyzer.create_frequent_words()
    analyzer.create_common_words()


if __name__ == "__main__":
    main()
