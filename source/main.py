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
            print("\tX: ", X, "\n\tY:", Y, f"\n\tZakres: <{rang[0]}, {rang[1]}>", "\n\tFunkcja: ", Functions.function_name(func))
            user_input = input('''Podaj, czy chcesz:
            (1) Wprowadzić węzły (ręcznie)
            (2) Wprowadzić węzły (plik)
            (3) Wybrać funkcję (prefediniowana)
            (4) Wybrać funkcję (własna)
            (5) Podać zakres
            (6) Obliczyć interpolację
            [q - wyjście]\n> ''')
            match user_input:
                case '1':
                    X , Y = array_from_user_input()
                case '2':
                    path = input(f"Podaj ścieżkę [{path}]: ")
                    X, Y = array_from_file(path)
                case '3':
                    func = choose_function() if not 0 else func
                case '4':
                    # TODO
                    pass
                case '5':
                    rang = [int(x) for x in input("Podaj dwie liczby oddzielone spacją: > ").split()]
                case '6':
                    draw_plot(X, Y, rang, func)
                case 'q':
                    break
                case _:
                    continue
            print()
            
        except ValueError:
            print("Podczas podawania parsowania macierzy wystąpił błąd. Sprawdź poprawność wprowadzanych danych.")


def draw_plot(X : np.array, Y : np.array, range : np.array, interpolation_func):
    arguments = ni.newton_interpolation(X, Y)
    # Debug
    #print(arguments)
    plot = ch.Plot(range[0], range[1])
    plot.draw_func(interpolation_func)
    plot.draw_interpolation(X, arguments)
    plot.draw_points(X, Y)
    plot.show()


class Functions:
    f_linear = lambda x: x
    f_absolute = lambda x: abs(x)
    f_polynomial = lambda x : 3*x**2 + 5*x - 10
    f_polynomial_unplural = lambda x : 10*x**4 + 5*x**3 - 50*x**2 + 20
    f_sinus = lambda x: np.sin(x)

    def function_name(func):
        match func:
            case Functions.f_linear: return "liniowa"
            case Functions.f_absolute : return "wartość bezwzględna"
            case Functions.f_polynomial : return "wielomianowa drugiego stopnia"
            case Functions.f_polynomial_unplural : return "wielomianowa trzeciego stopnia"
            case Functions.f_sinus : return "trygonometryczna (sinus)"

def choose_function():
    user_input = input(f'''Podaj numer funkcji:
    (1) {Functions.function_name(Functions.f_linear)}
    (2) {Functions.function_name(Functions.f_absolute)}
    (3) {Functions.function_name(Functions.f_polynomial)}
    (4) {Functions.function_name(Functions.f_polynomial_unplural)}
    (5) {Functions.function_name(Functions.f_sinus)}\n> ''')
    match user_input:
        case '1': return Functions.f_linear
        case '2': return Functions.f_absolute
        case '3': return Functions.f_polynomial
        case '4': return Functions.f_polynomial_unplural
        case '5': return Functions.f_sinus
        case _: return 0


if __name__ == "__main__":
    main()