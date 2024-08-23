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
    print(f"{Colors.BOLD}Error: {Colors.RED}\
          {message}{Colors.RESET}", file=sys.stderr)
    sys.exit(1)


def main():
    try:
        if len(sys.argv) == 1:
            print("What is the text to count?")
            string = input()
        elif len(sys.argv) == 2:
            string = sys.argv[1]
        else:
            print_error("You must provide one or zero arguments")
        if not string:
            print_error("You must provide a valid argument")
    except EOFError:
        print_error("Failed to read input")

    upper = 0
    lower = 0
    punctuation = 0
    digits = 0
    spaces = 0

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
    main()
