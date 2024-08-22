def main():
    # Original Objects
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    str_to_replace = ["World", "Portugal", "Porto", "42Porto"]

    # Modify the string of each data object
    # List -> Lists allow duplicate elements and can be modified
    # Tuple -> Tuples allow duplicate elements but cannot be modified
    # Set -> Sets do not allow duplicate elements and can be modified
    # Dict -> Dictionaries do not allow duplicate keys but can be modified

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
