import sys


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


def main():
    """
    Encodes a string argument into Morse code and prints it.
    """
    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        morse_code = ""
        for char in sys.argv[1]:
            if char.upper() in NESTED_MORSE:
                morse_code += NESTED_MORSE[char.upper()]
            else:
                raise AssertionError("the arguments are bad")

        print(morse_code.strip())
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
