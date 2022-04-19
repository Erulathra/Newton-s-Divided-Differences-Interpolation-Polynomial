from ast import FunctionDef, Lambda
import numpy as np
import newton_interpolation as ni
import charts as ch
from read_input import array_from_file, array_from_user_input


def main():
    X = np.array([-1, 1, 1.5, 2.3, 3, 3.14, 5, 7])
    Y = np.sin(X)
    func = Functions.f_sinus
    rang = [-1, 7]
    user_input = ""
    path = "../plik.csv"
    while user_input != "q":
        try:
            print(f"\tX: {X}")
            print(f"\tY: {Y}")
            print(f"\tZakres: <{rang[0]}, {rang[1]}>")
            print(f"\tFunkcja: {Functions.function_name(func)}")
            print(f"")

            user_input = input('''Podaj, czy chcesz:
            (1) Wprowadzić węzły (ręcznie)
            (2) Wprowadzić węzły (plik)
            (3) Wybrać funkcję (prefediniowana)
            (4) Podać zakres
            (5) Obliczyć interpolację
            [q - wyjście]\n> ''')
            match user_input:
                case '1':
                    X, Y = array_from_user_input()
                    func = None
                    rang = [np.min(X), np.max(X)]
                case '2':
                    path = input(f"Podaj ścieżkę [{path}]: ")
                    X, Y = array_from_file(path)
                    rang = [np.min(X), np.max(X)]
                    func = None
                case '3':
                    func = choose_function() if not 0 else func
                    X = get_X()
                    Y = func(X)
                    rang = [np.min(X), np.max(X)]
                case '4':
                    rang = [int(x) for x in input("Podaj dwie liczby oddzielone spacją: > ").split()]
                case '5':
                    draw_plot(X, Y, rang, func)
                case 'q':
                    break
                case _:
                    continue
            print()

        except ValueError:
            print("Podczas przetwarzania danych wystąpił błąd. Sprawdź poprawność wprowadzanych danych.")


def draw_plot(X: np.array, Y: np.array, range: np.array, interpolation_func):
    arguments = ni.newton_interpolation(X, Y)
    print("Obliczone współczynniki: ", arguments)
    plot = ch.Plot(range[0], range[1])

    if interpolation_func is not None:
        plot.draw_func(interpolation_func)

    plot.draw_interpolation(X, arguments)
    plot.draw_points(X, Y)
    plot.show()


class Functions:
    f_linear = lambda x: x
    f_absolute = lambda x: np.abs(x)
    f_polynomial = lambda x: 3 * x ** 2 + 5 * x - 10
    f_polynomial_unplural = lambda x: 10 * x ** 4 + 5 * x ** 3 - 50 * x ** 2 + 20
    f_sinus = lambda x: np.sin(x)
    f_complex = lambda x: x ** 2 + 20 * np.sin(x) - 10

    def function_name(func):
        match func:
            case Functions.f_linear:
                return "liniowa"
            case Functions.f_absolute:
                return "wartość bezwzględna"
            case Functions.f_polynomial:
                return "wielomianowa drugiego stopnia"
            case Functions.f_polynomial_unplural:
                return "wielomianowa trzeciego stopnia"
            case Functions.f_sinus:
                return "trygonometryczna (sinus)"
            case Functions.f_complex:
                return "złożona"


def choose_function():
    user_input = input(f'''Podaj numer funkcji:
    (1) {Functions.function_name(Functions.f_linear)}
    (2) {Functions.function_name(Functions.f_absolute)}
    (3) {Functions.function_name(Functions.f_polynomial)}
    (4) {Functions.function_name(Functions.f_polynomial_unplural)}
    (5) {Functions.function_name(Functions.f_sinus)}
    (6) {Functions.function_name(Functions.f_complex)}\n> ''')
    match user_input:
        case '1':
            return Functions.f_linear
        case '2':
            return Functions.f_absolute
        case '3':
            return Functions.f_polynomial
        case '4':
            return Functions.f_polynomial_unplural
        case '5':
            return Functions.f_sinus
        case '6':
            return Functions.f_complex
        case _:
            return 0


def get_X() -> np.ndarray:
    X_string = input("Podaj x odzielone spacją: \n").split(" ")
    return np.array(X_string, float)


if __name__ == "__main__":
    main()