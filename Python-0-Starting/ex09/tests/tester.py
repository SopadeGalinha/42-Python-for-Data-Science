# tests/tester.py
from ft_package import count_in_list


def test_count_in_list():
    assert count_in_list(["toto", "tata", "toto"], "toto") == 2
    assert count_in_list(["toto", "tata", "toto"], "tutu") == 0
    print("count_in_list tests passed!")


if __name__ == "__main__":
    test_count_in_list()
    print("\033[32mAll tests passed!\033[0m")
