import sys
from ft_filter import ft_filter


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
        f"{Colors.BOLD}AssertionError:"
        f"{Colors.RED} {message}{Colors.RESET}",
        file=sys.stderr
    )
    sys.exit(1)


def validate_args():
    """
Validate the arguments passed to the program
if the arguments are invalid, raise an AssertionError
with a message explaining the error."""

    assert len(sys.argv) == 3, "the argments are bad"
    assert sys.argv[2].isnumeric(), "the argments are bad"


def filterstring(string, integer):
    """
Filters a string based on the length of its words.
Args:
    string (str): The string to filter.
    integer (int): The minimum length of the words to keep.
Returns:
    list: A list of words that are longer than the specified length.
Raises:
    AssertionError: If the arguments are not valid.
Usage:
    filterstring("Hello, world!", 5)"""
    try:
        words = list(
            ft_filter(
                (lambda word: len(word) > integer),
                string.split()))
        return words
    except AssertionError as e:
        raise AssertionError(str(e))


def main():
    """
The main function of the filterstring program.
Usage:
    python3 filterstring.py "Hello, world!" 5
    """
    try:
        validate_args()
        words = filterstring(sys.argv[1], int(sys.argv[2]))
        print(words)
    except AssertionError as e:
        raise AssertionError(str(e))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print_error(str(e))
