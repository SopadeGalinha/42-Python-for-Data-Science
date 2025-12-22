import sys


def main():
    """
    Counts and displays character statistics from a string.
    Prompts for input if no argument provided.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1:
            print("What is the text to count?")
            string = input()
        else:
            string = sys.argv[1]
    except (AssertionError, EOFError) as e:
        if isinstance(e, EOFError):
            e = "EOFError occurred"
        raise AssertionError(str(e))

    upper = sum(c.isupper() for c in string)
    lower = sum(c.islower() for c in string)
    digits = sum(c.isdigit() for c in string)
    spaces = sum(c.isspace() for c in string)
    punctuation = len(string) - upper - lower - digits - spaces

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
        print(f"AssertionError: {e}")
