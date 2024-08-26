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
        f"{Colors.BOLD}AssertionError:"
        f"{Colors.RED} {message}{Colors.RESET}",
        file=sys.stderr
    )
    sys.exit(1)


NESTED_MORSE = {
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
    "Z": "--.. ", "0": "----- ", "1": ".---- ", "2": "..--- ",
    "3": "...-- ", "4": "....- ", "5": "..... ", "6": "-.... ",
    "7": "--... ", "8": "---.. ", "9": "----. ", " ": "/ "
}


def encode_to_morse(input_string):
    """
    Encodes the given input string to Morse code.
    Args:
        input_string (str): The string to be encoded.
    Returns:
        str: The Morse code representation of the input string.
    Raises:
        AssertionError: If the input string contains
         characters that are not supported by Morse code.
    """
    morse_code = ""
    for char in input_string:
        if char.upper() in NESTED_MORSE:
            morse_code += NESTED_MORSE[char.upper()]
        else:
            raise AssertionError("the arguments are bad")
    return morse_code.strip()


def main():
    """
    Main function that encodes a given input string
    into Morse Code and prints the result.
    Raises:
        AssertionError: If the number of arguments is not 1
        or if the argument is not a string.
    Usage:
        The main function expects a single command
        line argument, which should be a string.
        It converts the input string into Morse Code using
        the encode_to_morse function and prints the result.
    """
    try:
        # Verifica se o número de argumentos é 1
        assert len(sys.argv) == 2, "the arguments are bad"

        # Verifica se o argumento é uma string
        input_string = sys.argv[1]
        assert isinstance(input_string, str), "the arguments are bad"

        # Converte a string para Morse Code
        morse_code = encode_to_morse(input_string)
        print(morse_code)
    except AssertionError as e:
        print_error(str(e))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print_error(str(e))
