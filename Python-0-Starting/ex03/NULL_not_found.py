def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif object != object:
        print(f"Cheese: nan {type(object)}")
    elif object == 0 and type(object) is int:
        print(f"Zero: {object} {type(object)}")
    elif object == '':
        print(f"Empty: {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0
