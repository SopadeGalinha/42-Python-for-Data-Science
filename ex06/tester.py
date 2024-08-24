import ft_filter


class Colors:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    RESET = '\033[0;0m'


def test_ft_filter():
    """Test ft_filter function"""
    try:
        def is_even(n):
            return n % 2 == 0

        def is_odd(n):
            return n % 2 != 0

        def is_positive(n):
            return n > 0

        def is_non_negative(n):
            return n >= 0

        # Test 1: Filter even numbers
        numbers = [1, 2, 3, 4, 5, 6]
        result = list(ft_filter.ft_filter(is_even, numbers))
        assert result == [2, 4, 6], f"Test 1 Failed: {result}"

        # Test 2: Filter odd numbers
        result = list(ft_filter.ft_filter(is_odd, numbers))
        assert result == [1, 3, 5], f"Test 2 Failed: {result}"

        # Test 3: Filter positive numbers
        numbers = [-3, -2, -1, 0, 1, 2, 3]
        result = list(ft_filter.ft_filter(is_positive, numbers))
        assert result == [1, 2, 3], f"Test 3 Failed: {result}"

        # Test 4: Filter non-negative numbers
        result = list(ft_filter.ft_filter(is_non_negative, numbers))
        assert result == [0, 1, 2, 3], f"Test 4 Failed: {result}"

        # Test 5: Filter for truthy values
        values = [0, 1, '', 'text', None, True]
        result = list(ft_filter.ft_filter(None, values))
        assert result == [1, 'text', True], f"Test 5 Failed: {result}"

        # Test 6: Filter for falsy values
        result = list(ft_filter.ft_filter(lambda x: not x, values))
        assert result == [0, '', None], f"Test 6 Failed: {result}"

        # Test 7: Empty list
        result = list(ft_filter.ft_filter(is_even, []))
        assert result == [], f"Test 7 Failed: {result}"

        # Test 8: Filter for falsy values
        result = list(ft_filter.ft_filter(None, [False, None, 0, '', [], {}]))
        assert result == [], f"Test 8 Failed: {result}"

        # Test 9: Filter for falsy values
        result = list(ft_filter.ft_filter(lambda x: False, [1, 2, 3]))
        assert result == [], f"Test 9 Failed: {result}"

        # Test 10: Filter for truthy values
        result = list(ft_filter.ft_filter(lambda x: True, [1, 2, 3]))
        assert result == [1, 2, 3], f"Test 10 Failed: {result}"
        print(f"{Colors.GREEN}All tests passed!{Colors.RESET}")
    except AssertionError as e:
        print(f"{Colors.RED}KO: {e}{Colors.RESET}")


if __name__ == "__main__":
    test_ft_filter()
