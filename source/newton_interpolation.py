import numpy as np


def newton_interpolation(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    if len(X) != len(Y):
        raise InputArraysHadDifferentLengthsException

    iteration_count = len(X)

    # add Y to first row of difference_quotients
    difference_quotients = [Y.tolist()]

    # find difference_quotients
    for i in range(iteration_count - 1):
        # find quotients i rank
        i_rank_quotients = []
        for j in range(iteration_count - i - 1):
            quotient = (difference_quotients[i][j + 1] - difference_quotients[i][j]) / (X[i + j + 1] - X[j])
            i_rank_quotients.append(quotient)

        difference_quotients.append(i_rank_quotients)

    # calculate polynomial arguments
    arguments = []
    for i in range(iteration_count ):
        argument = difference_quotients[i][0]
        arguments.append(argument)

    return np.array(arguments)


def calculate_newton_polynomial(x: float, X: np.ndarray, arguments: np.ndarray) -> float:
    result = 0

    for i, argument in enumerate(arguments):
        # I didn't know how to name this float.
        # It stores product of (x - X1)(x - X2)(x - Xn)
        brackets = 1
        for j in range(1, i + 1):
            brackets *= x - X[j-1]

        result += argument * brackets

    return result


class InputArraysHadDifferentLengthsException(Exception):
    pass
