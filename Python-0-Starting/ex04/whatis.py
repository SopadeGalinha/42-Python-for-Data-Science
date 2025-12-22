import sys

try:
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        if n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
except AssertionError as e:
    print(f"AssertionError: {e}")
