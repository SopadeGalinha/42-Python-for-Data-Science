import pandas as pd  # type: ignore


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV file and return None when it cannot be read."""
    try:
        data = pd.read_csv(path)
        print(
            f"Loading dataset of dimensions "
            f"({data.shape[0]}, {data.shape[1]})"
        )
        return data
    except Exception as error:
        print(f"Error loading file {path}: {error}")
    return None
