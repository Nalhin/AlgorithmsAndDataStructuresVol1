/**
 * Returns index of first occurrence of a given value in an array utilizing linear search algorithm.
 *
 * @param {number[]} array
 * @param {number} valueToFind
 * @returns {?number} Index of first occurrence of `valueToFind`.
 */
export function linearSearch(array: number[], valueToFind: number) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === valueToFind) {
      return i;
    }
  }
  return null;
}
