/**
 * Returns index of first occurrence of a given value in an array utilizing binary search algorithm.
 *
 * @param {number[]} array - sorted array.
 * @param {number} searchedValue - value whose position is being searched.
 * @returns {?number} Index of the first occurrence of searched value.
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
