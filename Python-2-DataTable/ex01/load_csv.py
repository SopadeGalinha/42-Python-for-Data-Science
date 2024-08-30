import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data as a pandas DataFrame.

    Raises:
        FileNotFoundError: If the file is not found.
        pd.errors.ParserError: If there is an error parsing the file.
        Exception: If there is an unexpected error.
    """
    try:
        # Load the data
        data = pd.read_csv(path)
        if data.empty:
            print(f"Empty file: {path}")
            return None

        # Get the dimensions
        dimensions = data.shape
        print(
            f"Loading dataset of dimensions ({dimensions[0]},{dimensions[1]})")
        return data

    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except pd.errors.ParserError:
        print(f"Error parsing the file: {path}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
