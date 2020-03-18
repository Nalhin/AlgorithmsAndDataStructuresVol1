/**
 * Sorts a given array in place with quick sort algorithm.
 *
 * @param {number[]} array
 */
export function quickSort(array: number[]): void {
  quickSortRecursive(array, 0, array.length - 1);
}

/**
 * Recursive call to quick sort.
 *
 * @param {number[]} array
 * @param {number} low - index of first element
 * @param {number} high - index of last element
 */
function quickSortRecursive(array, low, high): void {
  if (low < high) {
    const pivot = randomPartition(array, low, high);
    quickSortRecursive(array, low, pivot - 1);
    quickSortRecursive(array, pivot + 1, high);
  }
}

/**
 * Chooses index used as pivot in partitioning
 *
 * @param {number[]} array
 * @param {number} p - index of first element
 * @param {number} r - index of last element
 */
function randomPartition(array, p, r): number {
  const random = Math.floor(Math.random() * (r - p)) + p;
  [array[random], array[r]] = [array[r], array[random]];
  return partition(array, p, r);
}

/**
 *
 * @param {number[]} array
 * @param {number} p - index of first element
 * @param {number} r - index of last element (pivot)
 *
 * @return {number} index of pivot element
 */
function partition(array: number[], p: number, r: number): number {
  let i = p;

  for (let j = p; j < r; j++) {
    if (array[j] <= array[r]) {
      [array[j], array[i]] = [array[i], array[j]];
      i++;
    }
  }

  [array[i], array[r]] = [array[r], array[i]];
  return i;
}
