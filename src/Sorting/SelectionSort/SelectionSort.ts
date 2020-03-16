/**
 * Sorts array in place with selection sort algorithm.
 *
 * @param {number[]} array
 */
export function selectionSort(array: number[]) {
  for (let i = 0; i < array.length; i++) {
    const smallest = findIndexOfSmallestElement(array, i);
    [array[i], array[smallest]] = [array[smallest], array[i]];
  }
}

/**
 * Finds the smallest element in array starting from initialIndex.
 *
 * @param {number[]} array
 * @param {number} initialIndex - starting position
 * @return {number} index of the smallest element in a given array.
 */
function findIndexOfSmallestElement(array: number[], initialIndex: number) {
  let smallestIndex = initialIndex;

  for (let i = initialIndex + 1; i < array.length; i++) {
    if (array[i] < array[smallestIndex]) {
      smallestIndex = i;
    }
  }

  return smallestIndex;
}
