def validate_input(family: list, start: int, end: int):
    """
    Validates the input parameters for the family list, start, and end.
    Parameters:
    family (list): A 2D list representing the family.
    start (int): The start index.
    end (int): The end index.
    Raises:
    AssertionError: If the family is not a 2D list,
                if the inner lists have different sizes,
                if the elements within the lists are not integers or floats,
                or if start and end are not integers.
    """
    # Check if the family is a 2D list

    if not isinstance(family, list) or not all(isinstance(row, list)
                                               for row in family):
        raise AssertionError(
            "The family must be a list of lists.")

    # Check if all inner lists have the same size
    if not all(len(row) == len(family[0]) for row in family):
        raise AssertionError(
            "All rows in the family list must be of the same length.")

    # Check if all elements within the lists are integers or floats
    if not all(isinstance(item, (int, float))
               for row in family for item in row):
        raise AssertionError(
            "All elements in the family list must be integers or floats.")

    # Check if start and end are integers
    if not isinstance(start, int) or not isinstance(end, int):
        raise AssertionError("Start and end must be integers.")


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a given list of lists (family) from the start index to the end index.
    Args:
        family (list): The list of lists to be sliced.
        start (int): The starting index of the slice.
        end (int): The ending index of the slice.
    Returns:
        list: The sliced list of lists.
    Raises:
        AssertionError:
        If the input is invalid (e.g. empty list, invalid start or end index).
    Example:
        family = [['John', 'Doe'], ['Jane', 'Smith'], ['Bob', 'Johnson']]
        start = 1
        end = 3
        sliced_family = slice_me(family, start, end)
        # Output: [['Jane', 'Smith'], ['Bob', 'Johnson']]
    """
    try:
        validate_input(family, start, end)

        # Print the original shape
        original_shape = (len(family), len(family[0]) if family else 0)
        print(f"My shape is : {original_shape}")
        # Perform the slicing
        sliced_family = family[start:end]
        # Print the new shape
        new_shape = (len(sliced_family),
                     len(sliced_family[0]) if sliced_family else 0)
        print(f"My new shape is : {new_shape}")
        return sliced_family

    except AssertionError as e:
        print(f"Error: {e}")
        return ""
