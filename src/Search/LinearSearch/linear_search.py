def linear_search(array, element_to_find):
    for index in range(len(array)):
        if array[index] == element_to_find:
            return index
    return None
