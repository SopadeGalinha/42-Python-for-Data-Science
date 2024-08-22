import sys


class Colors:
    RED = '\033[1;31m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def print_error(message):
    print(f"{Colors.BOLD}AssertionError: {Colors.RED}{message}{Colors.RESET}")
    sys.exit(1)


def is_even_or_odd(n):
    num_type = "Even" if n % 2 == 0 else "Odd"
    print(f"I'm {num_type}.")


def main():
    if len(sys.argv) != 2:
        error_message = "You must provide an argument" \
            if len(sys.argv) < 2 \
            else "More than one argument provided"
        print_error(error_message)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_error("Argument is not an integer")
    is_even_or_odd(n)


if __name__ == "__main__":
    main()
