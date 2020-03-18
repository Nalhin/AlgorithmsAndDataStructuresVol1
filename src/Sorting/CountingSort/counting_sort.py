def counting_sort(array, k):
    size = len(array)
    counter = [0] * k
    result = [0] * size

    for i in range(size):
        counter[array[i]] += 1

    for i in range(1, k):
        counter[i] += counter[i - 1]

    for i in range(size - 1, -1, -1):
        result[counter[array[i]] - 1] = array[i]
        counter[array[i]] -= 1

    return result
