import datetime


def main():
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
