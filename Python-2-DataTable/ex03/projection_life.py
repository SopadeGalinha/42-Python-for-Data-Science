from pathlib import Path

import matplotlib.pyplot as plt  # type: ignore
import pandas as pd  # type: ignore

from load_csv import load


def main() -> None:
    """Plot life expectancy against GDP for the year 1900."""
    try:
        gdp_path = Path(__file__).with_name(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_path = Path(__file__).with_name("life_expectancy_years.csv")
        gdp_data = load(str(gdp_path))
        life_data = load(str(life_path))
        if gdp_data is None or life_data is None:
            return
        points = gdp_data[["country", "1900"]].merge(
            life_data[["country", "1900"]],
            on="country",
            suffixes=("_gdp", "_life"),
        )
        points["1900_gdp"] = pd.to_numeric(points["1900_gdp"])
        points["1900_life"] = pd.to_numeric(points["1900_life"])
        points = points.dropna()

        plt.figure(figsize=(10, 6))
        plt.scatter(
            points["1900_gdp"], points["1900_life"],
            label="Countries", alpha=0.8,
        )
        plt.title("Life expectancy vs Gross domestic product (Year 1900)")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy (Years)")
        plt.xscale("log")

        plt.xticks(ticks=[300, 1000, 10000], labels=["300", "1k", "10k"])
        plt.legend()
        plt.tight_layout()
        plt.show()
    except Exception as error:
        print(f"Error preparing projection plot: {error}")


if __name__ == "__main__":
    main()
