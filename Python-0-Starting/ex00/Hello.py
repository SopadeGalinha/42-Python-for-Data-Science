def main():
    """
    This script demonstrates basic operations on different Python
    data structures (list, tuple, set, and dictionary)
    by modifying their elements.

    The operations include:
    - Modifying a list element
    - Creating a new tuple with updated values (since tuples are immutable)
    - Removing and adding elements in a set
    - Updating the value of a dictionary key

    Data Structures:
    1. List: Allows duplicates and is mutable.
    2. Tuple: Allows duplicates but is immutable.
    3. Set: Does not allow duplicates and is mutable.
    4. Dictionary: Does not allow duplicate keys and is mutable.
"""
    # Original Objects
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}
    str_to_replace = ["World", "Portugal", "Porto", "42Porto"]
    ft_list[1] = str_to_replace[0]  # Modify the string of the list
    ft_tuple = ("Hello", str_to_replace[1])  # Create a new tuple
    ft_set.remove("tutu!")  # Remove an element from the set
    ft_set.add(str_to_replace[2])  # Add a new element to the set
    ft_dict["Hello"] = str_to_replace[3]  # Modify the value of the key "Hello"

    # Display the modified objects
    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == '__main__':
    main()
