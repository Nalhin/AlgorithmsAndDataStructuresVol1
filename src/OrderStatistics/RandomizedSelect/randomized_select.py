from random import randint


def randomized_select(array, i):
    """return i smallest element of an array"""
    return randomized_select_recursive(array, 0, len(array) - 1, i)


def randomized_select_recursive(array, p, r, i):
    if p == r:
        return array[p]
    q = randomized_partition(array, p, r)
    k = q - p + 1
    if i == k:
        return array[q]
    if i < k:
        return randomized_select_recursive(array, p, q - 1, i)
    return randomized_select_recursive(array, q + 1, r, i - k)


def randomized_partition(array, p, r):
    rand = randint(p, r)
    array[r], array[rand] = array[r], array[rand]
    pivot = array[r]

    j = p
    for i in range(p, r):
        if array[i] < pivot:
            array[i], array[j] = array[j], array[i]
            j += 1

    array[r], array[j] = array[j], array[r]

    return j
