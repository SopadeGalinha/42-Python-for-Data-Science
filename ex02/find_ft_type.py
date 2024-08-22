def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)

    if obj_type == str:
        print(f"{object} is in the kitchen: {obj_type}")
    elif obj_type in [list, tuple, set, dict]:
        print(f"{obj_type.__name__.capitalize()} : {obj_type}")
    else:
        print("Type not found")
    return 42
