from array2D import slice_me


def tester():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))  # Expected: [[1.8, 78.4], [2.15, 102.7]]
    print(slice_me(family, 1, -2))  # Expected: [[2.15, 102.7]]


if __name__ == "__main__":
    tester()
