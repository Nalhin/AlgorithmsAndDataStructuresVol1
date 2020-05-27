from math import inf


def maximum_subarray_kadane(array):
    best_start = 0
    best_end = 0
    best_sum = -inf

    current_start = 0
    current_sum = 0

    for index, element in enumerate(array):
        current_sum += element
        if current_sum > best_sum:
            best_start = current_start
            best_end = index
            best_sum = current_start
        if current_sum < 0:
            current_start = index + 1
            current_sum = 0

    return array[best_start : best_end + 1]
