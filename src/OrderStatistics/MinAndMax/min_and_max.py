def min_and_max(array):
    """returns min and max values found in a given array"""
    n = len(array)
    minimum, maximum, initial = (array[0], array[0], 1) if n % 2 == 1 else (
        *get_smaller_and_greater(array[0], array[1]), 2)

    for i in range(initial, n, 2):
        smaller, greater = get_smaller_and_greater(array[i], array[i + 1])
        if smaller < minimum:
            minimum = smaller

        if greater > maximum:
            maximum = greater

    return minimum, maximum


def get_smaller_and_greater(a, b):
    """compare two elements then return smaller and greater"""
    if a < b:
        return a, b

    return b, a
