def heap_sort(array):
    build_max_heap(array)
    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, 0, i)


def build_max_heap(array):
    for i in range(len(array) // 2 - 1, -1, -1):
        max_heapify(array, i, len(array))


def max_heapify(array, i, heap_size):
    left = get_left_position(i)
    right = get_right_position(i)
    largest = i

    if left < heap_size and array[left] > array[i]:
        largest = left

    if right < heap_size and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest, heap_size)


def get_left_position(i):
    return i * 2 + 1


def get_right_position(i):
    return i * 2 + 2
