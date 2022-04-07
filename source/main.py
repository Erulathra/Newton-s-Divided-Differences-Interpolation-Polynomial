import numpy as np
import newton_interpolation as ni
import charts as ch


# TODO: delete this
def test_function(x):
    return np.sin(x)


def main():
    X = np.array([-1, 1, 1.5, 2.3, 3, 3.14, 5, 7])
    Y = np.sin(X)
    # X = np.array([0, 2, 3, 5, 6])
    # Y = np.array([0, 8, 27, 125, 216])

    arguments = ni.newton_interpolation(X, Y)
    print(arguments)

    plot = ch.Plot(-1, 7)
    plot.draw_func(test_function)
    plot.draw_interpolation(X, arguments)
    plot.draw_points(X, Y)
    plot.show()

if __name__ == "__main__":
    main()
