from main_setup import Setup, WebsiteAnalyzer


def main():
    WebsiteAnalyzer(
        top_frequency=1, languages="BOTH", action_type="BOTH", output_type="BOTH", run_type="read_websites")


if __name__ == "__main__":
    main()
