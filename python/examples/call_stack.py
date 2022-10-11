from math import sqrt


def calc_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def print_vector_length(x, y):
    length = calc_distance(x, y, 0, 0)
    print(length)


print_vector_length(3, 4)
