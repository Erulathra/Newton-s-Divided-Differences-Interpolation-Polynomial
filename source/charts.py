from matplotlib import pyplot
import numpy as np
import newton_interpolation as ni


class Plot:
    def __init__(self, minimum: float, maximum: float):
        figure: pyplot.Figure = pyplot.figure(dpi=200)
        self.__axes: pyplot.Axes = figure.subplots()

        self.__minimum = minimum
        self.__maximum = maximum
        pyplot.grid()
        pyplot.xlabel('X')
        pyplot.ylabel('y')

    def draw_func(self, func):
        plot_x = np.linspace(self.__minimum, self.__maximum, 300)
        plot_y = np.zeros(300)

        for i in range(300):
            plot_y[i] = func(plot_x[i])

        self.__axes.plot(plot_x, plot_y, 'r')

    def draw_points(self, X: np.ndarray, Y: np.ndarray):
        self.__axes.scatter(X, Y, c="g")

    def draw_interpolation(self, X: np.ndarray, arguments: np.ndarray):
        plot_x = np.linspace(self.__minimum, self.__maximum, 100)
        plot_y = np.zeros(100)

        for i in range(100):
            plot_y[i] = ni.calculate_newton_polynomial(plot_x[i], X, arguments)

        self.__axes.plot(plot_x, plot_y, 'b')

    def show(self):
        pyplot.show()
