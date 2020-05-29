/**
 * Randomizes an array in place.
 *
 * @param {number[]} array - array to randomize
 */

export function randomizeInPlace(array: number[]) {
  const n = array.length;

  for (let i = 0; i < n; i++) {
    const random = randomNumber(i, n);

    [array[i], array[random]] = [array[random], array[i]];
  }
}

/**
 * Generates random number in a given range.
 *
 * @param {number} min - minimum number
 * @param {number} max - maximum number
 *
 * @returns {number} random number in a given range.
 */
function randomNumber(min: number, max: number) {
  return Math.floor(Math.random() * (max - min)) + min;
}
