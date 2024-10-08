import sys


class Colors:
    """Class to hold color codes."""
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
    print(
        f"{Colors.BOLD}Error:"
        f"{Colors.RED} {message}{Colors.RESET}",
        file=sys.stderr
    )
    sys.exit(1)


def main():
    """
    Main function that reads/receives a string and counts the number of
    upper-case, lower-case, punctuation, digit and space characters
    in the string. It then displays the sums of each category.
    - If no arguments are provided, it prompts the user to enter a string.
    - If one argument is provided, it uses that as the string.
    - If more than one argument is provided, it displays an error message.
    - If any error occurs, it displays an error message.
    """
    try:
        assert (not len(sys.argv) > 2), "more than one argument is provided"
        if len(sys.argv) == 1 or sys.argv[1] is None:
            print("What is the text to count?")
            string = input()
        else:
            string = sys.argv[1]
    except (AssertionError, EOFError) as e:
        if isinstance(e, EOFError):
            e = "EOFError occurred"
        raise AssertionError(str(e))

    upper = 0
    lower = 0
    digits = 0
    spaces = 0
    punctuation = 0

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            punctuation += 1
    print(
        f"The text contains {len(string)} characters:\n"
        f"{upper} upper letters\n"
        f"{lower} lower letters\n"
        f"{punctuation} punctuation marks\n"
        f"{spaces} spaces\n"
        f"{digits} digits"
    )


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print_error(str(e))
