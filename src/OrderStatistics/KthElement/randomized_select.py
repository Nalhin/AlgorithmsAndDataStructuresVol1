from random import randint


def randomized_select(array, k):
    """Return k-th smallest element of an array"""
    return randomized_select_recursive(array, 0, len(array) - 1, k)


def randomized_select_recursive(array, low, high, k):
    if low == high:
        return array[low]
    pivot = randomized_partition(array, low, high)
    i = pivot - low + 1
    if k == i:
        return array[pivot]
    if k < i:
        return randomized_select_recursive(array, low, pivot - 1, k)
    return randomized_select_recursive(array, pivot + 1, high, k - i)


def randomized_partition(array, low, high):
    rand = randint(low, high)
    array[high], array[rand] = array[high], array[rand]
    pivot = array[high]

    j = low
    for i in range(low, high):
        if array[i] < pivot:
            array[i], array[j] = array[j], array[i]
            j += 1

    array[high], array[j] = array[j], array[high]

    return j
