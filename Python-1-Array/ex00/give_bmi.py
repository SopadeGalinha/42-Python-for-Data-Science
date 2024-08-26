def validate_bmi_input(
    height: list[int | float],
        weight: list[int | float]) -> None:

    if not all(isinstance(h, (int, float)) for h in height):
        raise ValueError(
            "All elements in the height list must be integers or floats.")
    for h in height:
        if h <= 0:
            raise ValueError(
                "All elements in the height list must be positive.")

    if not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError(
            "All elements in the weight list must be integers or floats.")
    for w in weight:
        if w <= 0:
            raise ValueError(
                "All elements in the weight list must be positive.")
    if len(height) != len(weight):
        raise ValueError(
            "Height and weight lists must be of the same length.")


def validate_limit_input(bmi: list[int | float], limit: int) -> None:
    if not isinstance(limit, int):
        raise ValueError("The limit must be an integer.")
    if limit <= 0:
        raise ValueError("The limit must be positive.")
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError(
            "All elements in the BMI list must be integers or floats.")
    if len(bmi) == 0:
        raise ValueError("The BMI list must not be empty.")


def give_bmi(
    height: list[int | float],
        weight: list[int | float]) -> list[int | float] | None:
    try:
        validate_bmi_input(height, weight)
        bmi_values = []
        for w, h in zip(weight, height):
            bmi = w / (h ** 2)
            bmi_values.append(bmi)
        return bmi_values
    except ValueError as e:
        print(f"Error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool] | None:
    try:
        validate_limit_input(bmi, limit)
        limit_reached = []
        for b in bmi:
            limit_reached.append(b >= limit)
        return limit_reached
    except ValueError as e:
        print(f"Error: {e}")
        return []
