import numpy as np
import csv

from pyparsing import string_start


def array_from_file(path) -> (np.array, np.array):
	with open(path, "r") as csv_file:
		reader = csv.reader(csv_file)
		result = []
		for line in reader:
			result.append([float(char) for char in line])
	return (np.array(result[0], float), np.array(result[1], float))


def array_from_user_input() -> (np.array, np.array):
	string_array = input('''Wprowadź punkty, oddzielając X i Y spacją, a węzły średnikami, np:\n\
		3 4; 5 1; 2 5; 8 4; 9 2; 3 5\n> ''')
	string_array = [line.split() for line in string_array.split(";")]
	for point in string_array:
		x, y = point
	return (np.array(x, float), np.array(y, float))
