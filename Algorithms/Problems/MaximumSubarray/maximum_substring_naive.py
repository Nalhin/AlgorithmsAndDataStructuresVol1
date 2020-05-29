from math import inf


def maximum_subarray_naive(array):
    max_val = -inf
    max_end = 0
    max_start = 0

    for i in range(len(array)):
        curr_sum = 0
        for j in range(i, len(array)):
            curr_sum += array[j]
            if curr_sum > max_val:
                max_val = curr_sum
                max_end = j
                max_start = i

    return array[max_start : max_end + 1]
