# tests/tester.py
from ft_package import *

def test_count_in_list():
    assert count_in_list(["toto", "tata", "toto"], "toto") == 2
    assert count_in_list(["toto", "tata", "toto"], "tutu") == 0

def test_ft_tqdm():
    from ft_package import ft_tqdm
    import time
    for _ in ft_tqdm(range(10)):
        time.sleep(0.1)


if __name__ == "__main__":
    test_count_in_list()
    test_ft_tqdm()
    print("\033[32mAll tests passed!\033[0m")
