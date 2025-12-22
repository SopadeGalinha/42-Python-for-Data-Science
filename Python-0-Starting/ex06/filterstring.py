import sys
from ft_filter import ft_filter


def main():
    """
    Filters words from a string based on their length.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].isnumeric(), "the arguments are bad"

        string = sys.argv[1]
        n = int(sys.argv[2])

        words = list(ft_filter(lambda word: len(word) > n, string.split()))
        print(words)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
