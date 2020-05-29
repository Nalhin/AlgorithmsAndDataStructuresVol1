import math
from itertools import chain

from Algorithms.Sorting.InsertionSort.insertion_sort import insertion_sort


def bucket_sort(array):
    n = len(array)

    buckets = [[] for _ in range(n)]

    for i in range(n):
        buckets[math.floor(n * array[i])].append(array[i])

    for i in range(n):
        insertion_sort(buckets[i])

    return list(chain(*buckets))
