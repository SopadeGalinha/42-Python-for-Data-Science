from give_bmi import give_bmi, apply_limit


def main():
    """Run a BMI calculation example and print results.

    This function is intended as a simple demonstration of the
    `give_bmi` and `apply_limit` helpers.
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
# Output:
    # [22.507863455018317, 29.0359168241966] <class 'list'>
    # [False, True]
