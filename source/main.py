import numpy as np
import newton_interpolation as ni


def main():
    # X = np.array([1, 3, 5, 7])
    # Y = np.array([2, 10, 26, 50])

    X = np.array([0, 2, 3, 5, 6])
    Y = np.array([0, 8, 27, 125, 216])

    result = ni.newton_interpolation(X, Y)
    print(result)


if __name__ == "__main__":
    main()
