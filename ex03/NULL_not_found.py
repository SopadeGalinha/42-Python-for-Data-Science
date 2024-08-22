def NULL_not_found(object: any) -> int:
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
