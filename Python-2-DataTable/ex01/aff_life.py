from pathlib import Path

import matplotlib.pyplot as plt  # type: ignore

from load_csv import load


def main() -> None:
    """Plot Portugal's life expectancy projection."""
    try:
        country_name = "Portugal"
        data_path = Path(__file__).with_name("life_expectancy_years.csv")
        dataset = load(str(data_path))
        if dataset is None:
            return
        country_data = dataset[dataset["country"] == country_name]
        if country_data.empty:
            print(f"Country not found: {country_name}")
            return
        years = country_data.columns[1:].astype(int)
        life_expectancy = country_data.iloc[0, 1:].astype(float)
        plt.plot(years, life_expectancy, label=country_name)
        plt.title(
            f"Life Expectancy in {country_name} Over the Years")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.xticks(years[::40], rotation=45)
        plt.yticks(range(30, 101, 10))
        plt.legend()
        plt.tight_layout()
        plt.show()
    except Exception as error:
        print(f"Error preparing life expectancy plot: {error}")


if __name__ == "__main__":
    main()
