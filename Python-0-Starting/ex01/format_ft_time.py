import datetime


def main():
    """
    This script demonstrates how to retrieve and
    display the current date and time using Python's `datetime` module.
    It also formats and presents the timestamp
    value in both regular and scientific notation.

    The script performs the following tasks:
    1. Retrieves the current date and time.
    2. Calculates and displays the number of seconds since January 1, 1970
    (Unix Epoch) in both standard format with comma separation
    and scientific notation.
    3. Formats and displays the date
    in the format: "Month Day Year" (e.g., "Aug 23 2024").

    Usage:
    Run the script to see the formatted timestamp and date.

    """

    # Get the current date and time
    now = datetime.datetime.now()

    # Display the current date and time
    print(
        "Seconds since January 1, 1970: "
        "{:,.4f} or {:.2e} in scientific notation".format(
            now.timestamp(), now.timestamp()
        )
    )
    print(now.strftime("%b %d %Y"))


if __name__ == '__main__':
    main()
