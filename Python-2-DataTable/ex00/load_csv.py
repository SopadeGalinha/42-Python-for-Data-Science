from pathlib import Path

import pandas as pd  # type: ignore


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV file and return None when it cannot be read."""

    try:
        data = pd.read_csv(path)
        dims = data.shape
        print(f"Loading dataset of dimensions ({dims[0]}, {dims[1]})")
        return data
    except Exception as error:
        print(f"Error loading file {path}: {error}")
    return None


def main() -> None:
    """Run a basic test with the dataset provided for this exercise."""
    data_path = Path(__file__).with_name("life_expectancy_years.csv")
    print(load(str(data_path)))


if __name__ == "__main__":
    main()
