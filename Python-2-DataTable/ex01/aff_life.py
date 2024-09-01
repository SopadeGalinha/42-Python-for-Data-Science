from matplotlib import pyplot as plt
from load_csv import load


def main():
    """
    Main function that loads a CSV file, filters
    the dataset for a specific country,
    extracts years and life expectancy values,
    and plots the data on a 2D graph.
    Raises:
        ValueError: If the number of command line arguments is not 2,
                    if the input file
                    is not a CSV file, or
                    if the provided file does not exist.
        AssertionError: If an assertion error occurs.
        Exception: If any other exception occurs.
    """
    try:
        country_name = 'Portugal'

        # - Loads the dataset
        dataset = load("life_expectancy_years.csv")

        # - Filters the dataset to only include data for the given country
        country_data = dataset[dataset['country'] == country_name]

        # - Extracts the years and life expectancy values
        years = country_data.columns[1:]
        life_expectancy = country_data.values[0][1:]

        # - Plots the data on a 2D graph with years on the x-axis
        # and life expectancy on the y-axis
        plt.plot(years, life_expectancy, label=country_name)

        # Title
        plt.title(
            f'Life Expectancy in {country_name} Over the Years')

        # x and y axis labels
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')

        # - x-axis ticks and labels (every 40 years)
        #  with a 45-degree rotation
        plt.xticks(years[::40], rotation=45)

        # Set the y-axis ticks to be every 10 years from 30 to 100
        plt.yticks(range(30, 101, 10))

        # - Display a legend
        plt.legend()

        # Adjusts the layout of the plot to make sure everything fits well,
        # especially when the axis labels are long or
        # the plot elements are close together.
        plt.tight_layout()

        # - Display the plot
        plt.show()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1
    except Exception as e:
        print(f"Exception: {e}")
        return 1


if __name__ == '__main__':
    main()
