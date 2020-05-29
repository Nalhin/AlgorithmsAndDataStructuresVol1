def quick_sort_hoare(array):
    quick_sort_recursive(array, 0, len(array) - 1)


def quick_sort_recursive(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quick_sort_recursive(array, low, pivot - 1)
        quick_sort_recursive(array, pivot + 1, high)


def partition(array, low, high):
    pivot = array[(low + high) // 2]

    left = low - 1
    right = high + 1

    while True:
        while True:
            left += 1
            if not array[right] < pivot:
                break

        while True:
            right -= 1
            if not array[right] > pivot:
                break

        if left >= right:
            return right
        array[left], array[right] = array[right], array[left]
