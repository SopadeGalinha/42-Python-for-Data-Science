def ft_filter(function, iterable):
    """filter(function or None, iterable) --> ft_filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    for item in iterable:
        if function is None:
            if item:
                yield item
        else:
            if function(item):
                yield item


def main():
    filtered = ft_filter(None, ["a", "b", "", "d"])
    print(list(filtered))


if __name__ == "__main__":
    main()
