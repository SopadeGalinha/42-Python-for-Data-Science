def validate_bmi_input(
    height: list[int | float],
        weight: list[int | float]) -> None:

    """Validate that height and weight lists are well-formed.

    This helper ensures both lists contain only positive numbers and have the
    same length.

    Args:
        height (list[int|float]): Heights in meters.
        weight (list[int|float]): Weights in kilograms.

    Raises:
        AssertionError: If inputs are not the expected types/values.
    """

    if not all(isinstance(h, (int, float)) for h in height):
        raise AssertionError(
            "All elements in the height list must be integers or floats.")
    for h in height:
        if h <= 0:
            raise AssertionError(
                "All elements in the height list must be positive.")

    if not all(isinstance(w, (int, float)) for w in weight):
        raise AssertionError(
            "All elements in the weight list must be integers or floats.")
    for w in weight:
        if w <= 0:
            raise AssertionError(
                "All elements in the weight list must be positive.")
    if len(height) != len(weight):
        raise AssertionError(
            "Height and weight lists must be of the same length.")


def validate_limit_input(bmi: list[int | float], limit: int) -> None:

    """Validate that the BMI list and limit value are valid.

    Args:
        bmi (list[int|float]): Computed BMI values.
        limit (int): The threshold value to compare against.

    Raises:
        AssertionError: If inputs are not the expected types/values.
    """
    if not isinstance(limit, int):
        raise AssertionError("The limit must be an integer.")
    if limit <= 0:
        raise AssertionError("The limit must be positive.")
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise AssertionError(
            "All elements in the BMI list must be integers or floats.")
    if len(bmi) == 0:
        raise AssertionError("The BMI list must not be empty.")


def give_bmi(
    height: list[int | float],
        weight: list[int | float]) -> list[int | float] | None:

    """Compute BMI values for paired height/weight lists.

    Args:
        height (list[int|float]): Heights in meters.
        weight (list[int|float]): Weights in kilograms.

    Returns:
        list[float] | None: List of BMI values or an empty string on error.
    """
    try:
        validate_bmi_input(height, weight)
        bmi_values = []
        for w, h in zip(weight, height):
            bmi = w / (h ** 2)
            bmi_values.append(bmi)
        return bmi_values
    except AssertionError as e:
        print(f"Error: {e}")
        return ""


def apply_limit(bmi: list[int | float], limit: int) -> list[bool] | None:

    """Apply a threshold to a list of BMI values.

    Args:
        bmi (list[int|float]): BMI values to check.
        limit (int): Threshold value.

    Returns:
        list[bool] | None: Boolean list for values exceeding the limit.
    """
    try:
        validate_limit_input(bmi, limit)
        limit_reached = []
        for b in bmi:
            limit_reached.append(b >= limit)
        return limit_reached
    except AssertionError as e:
        print(f"Error: {e}")
        return ""
