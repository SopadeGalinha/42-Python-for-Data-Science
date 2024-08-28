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


def print_rows(arr):
    """
    Prints the rows of a given array.

    Parameters:
    arr (list): The input array.

    Returns:
    None
    """
    count = 0
    for row in arr:
        count += 1
    length = count
    count = 0
    for row in arr:
        if count == 0:
            print("[[[", row[0], "]", sep="")
        if count > 0 and count < 3 or count > length - 4:
            if int == 1:
                if count == length - 1:
                    print("  [", row[0], "]]]", sep="")
                elif count < length - 1:
                    print("  [", row[0], "]", sep="")
            else:
                if count == length - 1:
                    print("  ", row[0], "]]", sep="")
                else:
                    print("  ", row[0], sep="")
        if count == 2:
            print("  ...")
        count += 1


def ft_transpose(matrix):
    """
    Transposes a 2D array.

    Args:
        matrix (numpy.ndarray): The input matrix to be transposed.

    Returns:
        numpy.ndarray: The transposed matrix.

    Raises:
        ValueError: If the input matrix is not at least a 2D array.
    """
    if matrix.ndim < 2:
        raise ValueError("Input must be at least a 2D array.")

    # Transpose the matrix using list comprehension for 2D array
    transposed_matrix = np.array(
        [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))])
    return transposed_matrix


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
        if len(sys.argv) != 2:
            raise AssertionError("Usage: python zoom.py <image_path>")
        path = sys.argv[1]
        if not os.path.exists(path):
            raise AssertionError("File not found.")
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("Unsupported image format.")
        img = ft_load(path)
        if len(img.shape) != 3 or img.shape[2] != 3:
            raise AssertionError(
                "The image is not in the expected format (HxWx3).")
        img_gray = ft_mean(img, axis=2)
        img_zoom = Image.fromarray(img_gray).crop((400, 100, 800, 500))
        print(f"The shape of image is: {img_zoom.size}")
        print_rows(np.array(img_zoom))
        img_zoom = ft_transpose(np.array(img_zoom))
        print(f"New shape after Transpose: {img_zoom.shape}")
        print(img_zoom)
        plt.imshow(img_zoom, cmap="gray")
        plt.axis("on")
        plt.show()
    except AssertionError as e:
        print(f"Error: {e}")
        return ""


if __name__ == "__main__":
    main()
