# Write a function that prints the object types and returns 42.
# 	Here’s how it should be prototyped:
# 		def all_thing_is_obj(object: any) -> int:
# 			#your code here
# 	Your tester.py:
# 		from find_ft_type import all_thing_is_obj
# 		ft_list = ["Hello", "tata!"]
# 		ft_tuple = ("Hello", "toto!")
# 		ft_set = {"Hello", "tutu!"}
# 		ft_dict = {"Hello" : "titi!"}
# 		all_thing_is_obj(ft_list)
# 		all_thing_is_obj(ft_tuple)
# 		all_thing_is_obj(ft_set)
# 		all_thing_is_obj(ft_dict)
# 		all_thing_is_obj("Brian")
# 		all_thing_is_obj("Toto")
# 		print(all_thing_is_obj(10))

# $>python tester.py | cat -e
# List : <class 'list'>$
# Tuple : <class 'tuple'>$
# Set : <class 'set'>$
# Dict : <class 'dict'>$
# Brian is in the kitchen : <class 'str'>$
# Toto is in the kitchen : <class 'str'>$
# Type not found$
# 42$
# $>

def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    
    if obj_type == str:
        print(f"{object} is in the kitchen : {obj_type}")
    elif obj_type == list or obj_type == tuple or obj_type == set or obj_type == dict:
        print(f"{obj_type.__name__.capitalize()} : {obj_type}")
    else:
        print(f"Type not found")
    return 42
