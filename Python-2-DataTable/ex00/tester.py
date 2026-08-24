from load_csv import load


def main() -> None:
    """Load the sample dataset and print its content."""
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
