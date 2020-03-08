/**
 * Returns index of first occurrence of a given value in an array utilizing binary search algorithm.
 *
 * @param {number[]} array - Sorted array.
 * @param {number} searchedValue - Value whose position is being searched.
 * @returns {?number} - Index of the first occurrence of `searchedValue`.
 */
export function binarySearch(array: number[], searchedValue: number) {
  let lower = 0;
  let upper = array.length - 1;

  while (lower <= upper) {
    const splitPosition = Math.floor((lower + upper) / 2);
    if (array[splitPosition] < searchedValue) {
      lower = splitPosition + 1;
    } else if (array[splitPosition] > searchedValue) {
      upper = splitPosition - 1;
    } else {
      return splitPosition;
    }
  }
  return null;
}
