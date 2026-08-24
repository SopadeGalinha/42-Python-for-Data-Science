from pathlib import Path

import matplotlib.pyplot as plt  # type: ignore
import pandas as pd  # type: ignore

from load_csv import load


def preprocess_population(population: str) -> float:
    """Convert a population value with an optional suffix to a number."""
    suffixes = {"k": 1e3, "M": 1e6, "B": 1e9}
    multiplier = suffixes.get(population[-1], 1)
    value = population[:-1] if multiplier != 1 else population
    return float(value) * multiplier


def plot_population_for_countries(
        data: pd.DataFrame, countries: list[str]) -> None:
    """Plot population projections for the selected countries."""
    plt.figure(figsize=(10, 6))

    max_population = 0.0
    years = None

    for country in countries:
        country_data = data[data["country"] == country].iloc[:, 1:]

        if years is None:
            years = country_data.columns.astype(int)

        if country_data.empty:
            print(f"Country not found: {country}")
            continue
        population = [
            preprocess_population(value)
            for value in country_data.iloc[0].tolist()
        ]

        plt.plot(years, population, label=country)
        max_population = max(max_population, max(population))

    plt.title("Population Comparison of Selected Countries")
    plt.xlabel("Year")
    plt.xticks(range(1800, 2051, 40))
    plt.xlim(1800, 2050)
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()

    y_ticks = [i * 1e7 for i in range(int(max_population / 1e7) + 2)]
    plt.yticks(y_ticks, [f"{pop / 1e6:,.0f}M" for pop in y_ticks])

    plt.show()


def main() -> None:
    """Plot Portugal's population against France's population."""
    try:
        data_path = Path(__file__).with_name("population_total.csv")
        data = load(str(data_path))
        if data is None:
            return
        countries = ["Portugal", "France"]
        plot_population_for_countries(data, countries)
    except Exception as error:
        print(f"Error preparing population plot: {error}")


if __name__ == "__main__":
    main()
