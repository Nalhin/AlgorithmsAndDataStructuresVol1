def linear_search(array, element_to_find):
    for index, el in enumerate(array, start=0):
        if el == element_to_find:
            return index
    return None
