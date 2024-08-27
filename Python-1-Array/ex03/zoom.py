from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os


def ft_mean(img, axis):
    """
    Compute the mean of a 3D array along a specified axis.
    Parameters:
    img (ndarray): The input 3D array.
    axis (int): The axis along which to compute the mean. Must be 2.
    Returns:
    ndarray: The grayscale image obtained by
        computing the mean along the specified axis.
    Raises:
    ValueError: If the input is not a 3D array or the axis is not 2.
    """
    # Validate that the input is a 3D array and axis is 2
    if len(img.shape) != 3 or axis != 2:
        raise ValueError("Input must be a 3D array, and axis must be 2.")

    # Compute the mean across the specified axis (axis=2 for color channels)
    grayscale_img = np.sum(img, axis=axis) / img.shape[axis]

    # Convert the result to uint8 (standard image format)
    return grayscale_img.astype(np.uint8)


def main():
    """
    Load, process, and display an image based on command-line arguments.

    This function serves as the main entry point of the script. It loads an
    image from the command-line argument, performs various image processing
    operations, and displays the resulting images. The script supports
    cropping, grayscale conversion, and zoomed image display. Errors related
    to file format and existence are caught and displayed.
    """
    try:
        path = sys.argv[1]
        if not os.path.exists(path):
            raise AssertionError("File not found.")
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("Unsupported image format.")
        img = ft_load(path)
        # img_gray = ft_mean(img, 2)
        img_gray = np.mean(img, axis=2).astype(np.uint8)
        img_zoom = Image.fromarray(img_gray).crop((400, 100, 800, 500))
        img_zoom.save("zoomed_image.jpg")
        plt.imshow(img_zoom, cmap="gray")
        plt.axis("off")
        plt.show()
    except AssertionError as e:
        print(f"Error: {e}")
        return ""


if __name__ == "__main__":
    main()