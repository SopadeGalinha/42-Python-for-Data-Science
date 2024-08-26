import sys


class Colors:
    """
    Defines ANSI escape codes for colored and formatted terminal output.
    Attributes:
        RED (str): Escape code for red color text.
        BOLD (str): Escape code for bold text.
        RESET (str): Escape code to reset text formatting.
    """
    RED = '\033[1;31m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def print_error(message):
    """
    Prints an error message in bold red text and exits the program.
    Args:
        message (str): The error message to be displayed.
    Exits:
        The program exits with status code 1 after printing the error message.
    """
    print(f"{Colors.BOLD}AssertionError: {Colors.RED}{message}{Colors.RESET}")
    sys.exit(1)


def is_even_or_odd(n):
    """
    Determines whether a given integer is even or odd and prints the result.
    Args:
        n (int): The integer to be evaluated.
    Prints:
        A message indicating whether the number is "Even" or "Odd".
    """
    num_type = "Even" if n % 2 == 0 else "Odd"
    print(f"I'm {num_type}.")


def main():
    """
    Main function that validates the command-line argument and determines
    if it is even or odd.
    - Checks if exactly one command-line argument is provided.
    - Validates that the argument is an integer.
    - Calls `is_even_or_odd` to print whether the number is even or odd.
    If validation fails, it calls `print_error`
    to display an error message and exit.
    """
    if len(sys.argv) < 2:
        return
    assert len(sys.argv) == 2, "more than one argument is provided"
    try:
        n = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    is_even_or_odd(n)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print_error(str(e))
