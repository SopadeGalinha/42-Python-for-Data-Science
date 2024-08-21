from find_ft_type import all_thing_is_obj

# Define various objects to test
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Call the function with different objects
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")

# Print the result of calling the function with an integer
print(all_thing_is_obj(10))

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

# <class 'list'>$
# <class 'tuple'>$
# <class 'set'>$
# <class 'dict'>$
# <class 'str'>$
# <class 'str'>$
# <class 'int'>$
# 42$