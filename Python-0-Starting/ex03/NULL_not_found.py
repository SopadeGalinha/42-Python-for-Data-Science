def NULL_not_found(object: any) -> int:
    """
    Checks the input object against various common "null-like" conditions and
    prints a message based on the first match.

    Conditions (in order):
    - None: Prints "Nothing : None".
    - NaN: Prints "Cheese : NaN".
    - Zero: Prints "Zero".
    - Empty string: Prints "Empty".
    - False: Prints "Fake".
    """
    # Check conditions in a prioritized order
    if object is None:
        print(f"Nothing : None {type(object)}")
    elif object != object:
        print(f"Cheese : NaN {type(object)}")
    elif object == 0:
        print(f"Zero : {type(object)}")
    elif object == '':
        print(f"Empty : {type(object)}")
    elif object is False:
        print(f"Fake : {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0
