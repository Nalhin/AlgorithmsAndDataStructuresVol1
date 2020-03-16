def insertion_sort(array):
    for i in range(len(array)):
        curr = i - 1
        while curr >= 0 and array[curr] > array[curr+1]:
            array[curr], array[curr + 1] = array[curr + 1], array[curr]
            curr -= 1
