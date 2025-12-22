def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    elif type(object) in (list, tuple, set, dict):
        print(f"{type(object).__name__.capitalize()} : {type(object)}")
    else:
        print("Type not found")
    return 42
