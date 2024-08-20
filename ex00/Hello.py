#	You need to modify the string of each data object to display the following greetings:
# 	"Hello World",
# 	"Hello «country of your campus»",
# 	"Hello «city of your campus»", 
# 	"Hello «name of your campus»"

# Expected output:
# 	$>python Hello.py | cat -e
# 	['Hello', 'World!']$
# 	('Hello', 'France!')$
# 	{'Hello', 'Paris!'}$
# 	{'Hello': '42Paris!'}$
# 	$>

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
	
	ft_list[1] = str_to_replace[0] # Modify the string of the list
	ft_tuple = ("Hello", str_to_replace[1]) # Create a new tuple
	ft_set.remove("tutu!") # Remove an element from the set
	ft_set.add(str_to_replace[2]) # Add a new element to the set
	ft_dict["Hello"] = str_to_replace[3] # Modify the value of the key "Hello"
	
	# Display the modified objects
	print(ft_list)
	print(ft_tuple)
	print(ft_set)
	print(ft_dict)

if __name__ == '__main__':
	main()

# The purpose of the if __name__ == '__main__': statement is to ensure
# that the code inside it is only executed when the module is run directly,
# and not when it is imported as a module into another program.

# This is useful because sometimes a module may contain code that
# should only be executed when it is run as a standalone program, 
# but not when it is imported by other modules.

# By calling the main() function inside the if __name__ == '__main__': block,
# the code ensures that the main() function is only executed when
# the module is run as the main program. 
# This allows for better organization and separation of code logic.