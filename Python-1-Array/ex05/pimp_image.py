from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os
import array


def ft_invert(array) -> array:
	"""
	Invert the colors of an image.
	Parameters:
	array (ndarray): The input image.
	Returns:
	ndarray: The image with inverted colors.
	"""
	# Invert the colors of the image
	inverted_array = 255 - array
	return inverted_array


def ft_red(array) -> array:
	"""
	Extract the red channel of an image.
	Parameters:
	array (ndarray): The input image.
	Returns:
	ndarray: The red channel of the image.
	"""
	# Extract the red channel of the image
	red_array = array.copy()
	red_array[:, :, 1] = 0
	red_array[:, :, 2] = 0
	return red_array

def ft_green(array) -> array:
	"""
	Extract the green channel of an image.
	Parameters:
	array (ndarray): The input image.
	Returns:
	ndarray: The green channel of the image.
	"""
	# Extract the green channel of the image
	green_array = array.copy()
	green_array[:, :, 0] = 0
	green_array[:, :, 2] = 0
	Image.fromarray(green_array).show()
	return green_array


def ft_blue(array) -> array:
	"""
	Extract the blue channel of an image.
	Parameters:
	array (ndarray): The input image.
	Returns:
	ndarray: The blue channel of the image.
	"""
	# Extract the blue channel of the image
	blue_array = array.copy()
	blue_array[:, :, 0] = 0
	blue_array[:, :, 1] = 0
	Image.fromarray(blue_array).show()
	return blue_array


def ft_grey(array) -> array:
	"""
	Convert an image to grayscale.
	Parameters:
	array (ndarray): The input image.
	Returns:
	ndarray: The grayscale image.
	"""
	# Convert the image to grayscale
	grey_array = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
	Image.fromarray(grey_array).show()
	return grey_array
