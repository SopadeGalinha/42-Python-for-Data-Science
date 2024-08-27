from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.array:
    """
    Load an image from the given file path and return it as a NumPy array.
    Parameters:
    path (str): The file path of the image to be loaded.
    Returns:
    np.ndarray: The loaded image as a NumPy array.
    Raises:
    AssertionError:
        If the file is not found or if the image format is unsupported.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("File not found.")
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("Unsupported image format.")
        img = Image.open(path)
        print(
            f"The shape of Image is: {img.size[1]},{img.size[0]}, {img.layers}"
            )
        return np.array(img)
    except AssertionError as e:
        print(f"Error: {e}")
        return ""
