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
    for i in range(iteration_count - 1):
        argument = difference_quotients[i][0]
        arguments.append(argument)

    return np.array(arguments)


class InputArraysHadDifferentLengthsException(Exception):
    pass
