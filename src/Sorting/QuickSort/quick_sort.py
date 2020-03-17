from random import randint


def quick_sort(array):
    quick_sort_recursive(array, 0, len(array) - 1)


def quick_sort_recursive(array, p, r):
    if p < r:
        q = random_partition(array, p, r)
        quick_sort_recursive(array, p, q - 1)
        quick_sort_recursive(array, q + 1, r)


def random_partition(array, p, r):
    pivot = randint(p, r)
    array[pivot], array[r] = array[r], array[pivot]
    return partition(array, p, r)


def partition(array, p, r):
    x = array[r]
    i = p - 1

    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]

    q = i + 1
    array[q], array[r] = array[r], array[q]
    return q
