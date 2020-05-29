import random
import math


def permutate_by_sorting(array):
    n = len(array)
    order = [math.floor(random.randint(0, n ** 3)) for _ in range(n)]

    return [x for _, x in sorted(zip(order, array), key=lambda pair: pair[0])]
