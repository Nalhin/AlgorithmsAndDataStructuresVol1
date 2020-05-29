/**
 * Sorts a given array in place with merge sort algorithm.
 *
 * @param {number[]} array - array to sort
 */

export function mergeSort(array) {
  mergeSortRecursive(array, 0, array.length - 1);
}

/**
 * Recursive call to merge sort.
 *
 * @param {number[]} array - array to sort
 * @param low - index of first element
 * @param high - index of last element
 */
function mergeSortRecursive(array: number[], low: number, high: number) {
  if (low < high) {
    const middle = Math.floor((low + high) / 2);
    mergeSortRecursive(array, low, middle);
    mergeSortRecursive(array, middle + 1, high);
    mergeArray(array, low, middle, high);
  }
}

/**
 * Merges two sorted arrays in place
 * @param array - array to merge
 * @param low - index of the first element in sorted left slice
 * @param middle - index of the last element in sorted left slice
 * @param high - index of the last element in sorted right slice
 */
function mergeArray(
  array: number[],
  low: number,
  middle: number,
  high: number,
) {
  // slice it not inclusive
  const leftSlice = array.slice(low, middle + 1);
  const rightSlice = array.slice(middle + 1, high + 1);

  let right = 0;
  let left = 0;
  let merged = low;

  while (left < leftSlice.length && right < rightSlice.length) {
    if (leftSlice[left] <= rightSlice[right]) {
      array[merged] = leftSlice[left];
      left++;
    } else {
      array[merged] = rightSlice[right];
      right++;
    }
    merged++;
  }

  while (right < rightSlice.length) {
    array[merged] = rightSlice[right];
    merged++;
    right++;
  }

  while (left < leftSlice.length) {
    array[merged] = leftSlice[left];
    merged++;
    left++;
  }
}
