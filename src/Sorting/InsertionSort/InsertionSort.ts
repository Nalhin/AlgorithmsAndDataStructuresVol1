/**
 * Sorts given array in place with insertion sort algorithm.
 *
 * @param {number[]} array
 */
export function insertionSort(array: number[]) {
  for (let i = 1; i < array.length; i++) {
    let j = i - 1;
    while (j >= 0 && array[j] > array[j + 1]) {
      [array[j + 1], array[j]] = [array[j], array[j + 1]];
      j--;
    }
  }
}
