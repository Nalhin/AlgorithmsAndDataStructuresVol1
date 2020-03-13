/**
 * Randomly permutates an array utilizing permutate by sorting algorithm
 *
 * @param array - array to permutate.
 *
 * @return {number[]} - permutation of `array`.
 */
export function permutateBySorting(array: number[]) {
  const n = array.length;

  return array
    .map(val => ({
      val,
      test: Math.floor(Math.random() * Math.pow(n, 3)),
    }))
    .sort((a, b) => (a.test > b.test ? 1 : a.test === b.test ? 0 : -1))
    .map(a => a.val);
}
