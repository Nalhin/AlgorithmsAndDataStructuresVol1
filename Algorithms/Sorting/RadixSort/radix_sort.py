import math

NUM_OF_DIGITS = 10


def radix_sort(array):
    d = max_digits(array)
    exp = 1
    while d / exp > 0:
        counting_sort(array, exp)
        exp *= NUM_OF_DIGITS


def max_digits(array):
    return int(math.log10(max(array))) + 1


def counting_sort(array, exp):
    k = NUM_OF_DIGITS
    size = len(array)
    counter = [0] * k
    result = [0] * size

    for i in range(size):
        counter[get_index(array, exp, i)] += 1

    for i in range(1, k):
        counter[i] += counter[i - 1]

    for i in range(size - 1, -1, -1):
        result[counter[get_index(array, exp, i)] - 1] = array[i]
        counter[get_index(array, exp, i)] -= 1

    for i in range(len(array)):
        array[i] = result[i]


def get_index(array, exp, i):
    return int(array[i] / exp) % 10
