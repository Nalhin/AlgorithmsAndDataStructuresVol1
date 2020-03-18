from random import randint


def quick_sort_lomuto(array):
    quick_sort_recursive(array, 0, len(array) - 1)


def quick_sort_recursive(array, low, high):
    if low < high:
        pivot = random_partition(array, low, high)
        quick_sort_recursive(array, low, pivot - 1)
        quick_sort_recursive(array, pivot + 1, high)


def random_partition(array, low, high):
    pivot = randint(low, high)
    array[pivot], array[high] = array[high], array[pivot]
    return partition(array, low, high)


def partition(array, low, high):
    x = array[high]
    i = low

    for j in range(low, high):
        if array[j] <= x:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[high] = array[high], array[i]
    return i
