from load_image import ft_load


def tester():
    """Load a sample image and print its array representation."""
    print(ft_load("landscape.jpg"))

    # Display the image
    # from matplotlib import pyplot as plt
    # img_array = ft_load("landscape.jpg")
    # plt.imshow(img_array)
    # plt.show()


if __name__ == "__main__":
    tester()
