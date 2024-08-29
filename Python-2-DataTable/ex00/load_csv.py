# Make a function that takes a path as argument,
# writes the dimensions of the data set
# # and returns it. You have to handle the error cases
# and return None if the path is bad,
# bad format..


def load(path: str) -> list:
	try:
		with open(path, 'r') as f:
			data = f.read()
			data = data.split('\n')
			data = [x.split(',') for x in data]
			print(f"Dimensions: {len(data)}x{len(data[0])}")
			return data
	except AssertionError as e:
		print(f"Error: {e}")
		return None
	except FileNotFoundError as e:
		print(f"Error: {e}")
		return None
	except Exception as e:
		print(f"Error: {e}")
		return None

