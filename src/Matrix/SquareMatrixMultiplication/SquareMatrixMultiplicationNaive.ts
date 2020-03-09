/**
 * Returns the product of two matrices. Implemented with naive algorithm.
 *
 * @param {number[][]} A - Matrix.
 * @param {number[][]} B - Matrix.
 *
 * @returns {number[][]} The product of `A` and `B`.
 */

export function squareMatrixMultiplicationNaive(A: number[][], B: number[][]) {
  const product = [];
  const length = A.length;
  for (let i = 0; i < length; i++) {
    product[i] = [];
    for (let j = 0; j < length; j++) {
      product[i][j] = 0;

      for (let k = 0; k < length; k++) {
        product[i][j] += A[i][k] * B[k][j];
      }
    }
  }
  return product;
}
