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


def main():
    """
    Load, process, and display an image with zoom functionality.

    Loads "animal.jpeg", prints shape and pixel data, crops to zoom region,
    converts to grayscale, and displays with axis scales.
    """
    filename = "animal.jpeg"

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    try:
        img = ft_load(filename)

        print(f"The shape of image is: {img.shape}")
        print(img)

        # Convert to grayscale and crop
        img_gray = ft_mean(img, axis=2)
        img_zoom = img_gray[100:500, 400:800]

        # Add dimension to match expected output format (400, 400, 1)
        img_zoom_3d = np.expand_dims(img_zoom, axis=2)

        print(f"New shape after slicing: {img_zoom_3d.shape}")
        print(img_zoom_3d)

        # Display the zoomed image with axes
        plt.imshow(img_zoom, cmap="gray")
        plt.show()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
