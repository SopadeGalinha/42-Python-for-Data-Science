from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        # Load the GDP data for the year 1900
        gdp_file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        gdp_data = [load(gdp_file)['1900']]

        # Load the life expectancy data for the year 1900
        life_expectancy_data = [load("life_expectancy_years.csv")['1900']]

        plt.figure(figsize=(10, 6))
        # plt.plot(gdp_data, life_expectancy_data, 'o')
        plt.scatter(gdp_data, life_expectancy_data)
        plt.title("Life expectancy vs Gross domestic product (Year 1900)")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy (Years)")
        plt.xscale("log")

        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.tight_layout()
        plt.show()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
