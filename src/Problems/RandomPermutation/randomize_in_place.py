import random


def randomize_in_place(array):
    n = len(array)

    for i in range(n):
        rnd = random.randint(i, n - 1)
        array[rnd], array[i] = array[i], array[rnd]
