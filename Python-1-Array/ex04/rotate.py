from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
import os


def ft_mean(img, axis):
    """
    Convert RGB image to grayscale by computing mean of color channels.

    Args:
        img (ndarray): The input RGB image array with shape (height, width, 3).
        axis (int): The axis along which to compute the mean. Must be 2.

    Returns:
        ndarray: The grayscale image (2D array).

    Raises:
        ValueError: If the input is not a 3D array or axis is not 2.
    """
    if len(img.shape) != 3 or axis != 2:
        raise ValueError("Input must be a 3D array, and axis must be 2.")

    height, width, channels = img.shape
    grayscale_img = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            # Calculate mean of RGB values
            r, g, b = img[i, j]
            grayscale_img[i, j] = (int(r) + int(g) + int(b)) // 3

    return grayscale_img


def ft_transpose(matrix):
    """
    Transposes a 2D array without using any library functions.

    Args:
        matrix (numpy.ndarray): The input matrix to be transposed.

    Returns:
        list: The transposed matrix as a list of lists.

    Raises:
        ValueError: If the input matrix is not at least a 2D array.
    """
    if matrix.ndim < 2:
        raise ValueError("Input must be at least a 2D array.")

    # Transpose manually without using library functions
    height = len(matrix)
    width = len(matrix[0])
    transposed_matrix = []

    for i in range(width):
        row = []
        for j in range(height):
            row.append(matrix[j][i])
        transposed_matrix.append(row)

    return transposed_matrix


def main():
    """
    Load, process, and display a rotated grayscale image.

    Loads "animal.jpeg", converts to grayscale, crops, transposes,
    and displays the result with axis scales.
    """
    filename = "animal.jpeg"

    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    try:
        # Load image
        img = ft_load(filename)

        # Convert to grayscale and crop
        img_gray = ft_mean(img, axis=2)
        img_zoom = img_gray[100:500, 400:800]

        # Add dimension and print zoomed image
        img_zoom_3d = np.expand_dims(img_zoom, axis=2)
        print(f"The shape of image is: {img_zoom_3d.shape}")
        print(img_zoom_3d)

        # Transpose the image
        img_transposed = ft_transpose(img_zoom)
        new_height = len(img_transposed)
        new_width = len(img_transposed[0])
        print(f"New shape after Transpose: ({new_height}, {new_width})")
        print(np.array(img_transposed))

        # Display the transposed image with axes
        plt.imshow(img_transposed, cmap="gray")
        plt.show()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
