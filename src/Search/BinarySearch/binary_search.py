def binary_search_iterative(array, searched_value):
    lower = 0
    upper = len(array) - 1

    while lower <= upper:
        middle = (lower + upper) // 2
        if array[middle] < searched_value:
            lower = middle + 1
        elif array[middle] > searched_value:
            upper = middle - 1
        else:
            return middle

    return None


def binary_search_recursive(array, searched_value, lower=None, upper=None):
    if lower is None:
        lower = 0
    if upper is None:
        upper = len(array)

    middle = (lower + upper) // 2

    if lower == upper:
        return None

    if array[middle] == searched_value:
        return middle

    if array[middle] > searched_value:
        return binary_search_recursive(array, searched_value, middle + 1, upper)

    return binary_search_recursive(array, searched_value, lower, middle - 1)
