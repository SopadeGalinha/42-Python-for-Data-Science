from load_csv import load
import matplotlib.pyplot as plt


def preprocess_population(pop_str):
    """
    Preprocesses the population string to convert it into
    a numeric value in standard form.
    Args:
        pop_str (str): Population string with or without
        the 'M' suffix for million.
    Returns:
        float: Numeric population value.
    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("B"):
        return float(pop_str[:-1]) * 1e9
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def plot_population_for_countries(data, countries):
    """
    Plots the population data for a list of countries.

    Args:
        data (DataFrame): The population data loaded from the CSV.
        countries (list of str): List of country names to plot.
    """
    plt.figure(figsize=(10, 6))

    max_population = 0
    years = None

    for country in countries:
        country_data = data[data['country'] == country].iloc[:, 1:]

        if years is None:
            years = country_data.columns.astype(int)

        # Flatten the data into a 1D array
        population = country_data.values.flatten()

        # Preprocess the population data
        population = [preprocess_population(pop) for pop in population]

        plt.plot(years, population, label=country)
        max_population = max(max_population, max(population))

    plt.title("Population Comparison of Selected Countries")
    plt.xlabel("Year")
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()

    y_ticks = [i * 1e7 for i in range(int(max_population / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])

    plt.show()


def main():
    """
    Loads population data from a CSV file, processes, and
    plots the population comparison of the given countries.

    Args:
        countries (list of str): List of country names to plot.
    """
    try:
        data = load("population_total.csv")
        countries = ["Brazil", "Portugal", "France",
                    "Hungary", "Italy", "Spain", "Germany", "United States", "China"]
        plot_population_for_countries(data, countries)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1
    except Exception as e:
        print(f"Exception: {e}")
        return 1


if __name__ == "__main__":
    main()
