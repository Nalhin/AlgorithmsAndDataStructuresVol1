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
