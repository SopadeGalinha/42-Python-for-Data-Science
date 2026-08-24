# Python 2 - DataTable

Piscine Python for Data Science, module 2. This project introduces loading,
manipulating and displaying tabular data with `pandas` and `matplotlib`.

Data comes from the free school materials published by
[Gapminder.org](https://www.gapminder.org/) (CC-BY license).

## Requirements

- Python 3.10
- `pandas`
- `matplotlib`
- `flake8` (for norm checking)

## Setup

This project uses [uv](https://docs.astral.sh/uv/) to manage the virtual
environment and dependencies.

```sh
uv sync
```

Alternatively, with plain `pip`:

```sh
python3.10 -m venv .venv
source .venv/bin/activate
pip install pandas matplotlib flake8
```

## Project structure

```
ex00/  load_csv.py         load a CSV file into a DataFrame
ex01/  load_csv.py, aff_life.py     plot life expectancy for one country
ex02/  load_csv.py, aff_pop.py      compare population between countries
ex03/  load_csv.py, projection_life.py   life expectancy vs GDP (year 1900)
```

## Exercises

### ex00 - Load my Dataset

`load(path: str) -> pd.DataFrame | None` reads a CSV file, prints its
dimensions and returns the resulting DataFrame. It returns `None` and prints
an error message when the path is invalid or the file cannot be parsed.

```sh
cd ex00
python tester.py
```

### ex01 - Draw my country

Loads `life_expectancy_years.csv` and plots the life expectancy projection of
Portugal over time.

```sh
cd ex01
python aff_life.py
```

### ex02 - Compare my country

Loads `population_total.csv` and plots the population projection of Portugal
against France, from 1800 to 2050.

```sh
cd ex02
python aff_pop.py
```

### ex03 - Draw my year

Loads `income_per_person_gdppercapita_ppp_inflation_adjusted.csv` and
`life_expectancy_years.csv`, then plots life expectancy against gross
domestic product for the year 1900, for every country.

```sh
cd ex03
python projection_life.py
```

## Norm

Code style is checked with `flake8`:

```sh
flake8 ex00 ex01 ex02 ex03
```
