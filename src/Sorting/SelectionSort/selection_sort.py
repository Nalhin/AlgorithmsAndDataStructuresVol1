def selection_sort(array):
    for i in range(len(array)):
        smallest = find_index_of_smallest_element(array, i)
        array[i], array[smallest] = array[smallest], array[i]


def find_index_of_smallest_element(array, initial_index):
    smallest_index = initial_index
    for i in range(initial_index, len(array)):
        if array[smallest_index] > array[i]:
            smallest_index = i

    return smallest_index
