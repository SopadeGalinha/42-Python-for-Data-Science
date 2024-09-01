from S1E9 import Character, Stark


def main():
    try:
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)
        hodor = Character("Hodor")
        print(hodor.__dict__)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
