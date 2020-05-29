/**
 * Returns the product of two square matrices. Calculated with recursive algorithm.
 *
 * @param {number[][]} A - square matrix with the same size as `B`.
 * @param {number[][]} B - square matrix with the same size as `A`.
 *
 * @returns {number[][]} The product of `A` and `B`.
 */

export function squareMatrixMultiplicationRecursive(
  A: number[][],
  B: number[][],
) {
  return multiplyRecursively(
    A,
    B,
    { rows: 0, cols: 0 },
    { rows: 0, cols: 0 },
    A.length,
  );
}

interface MatrixSlicePositions {
  rows: number;
  cols: number;
}

/**
 * Recursively splits matrices into smaller ones and calculates their product.
 *
 * @param {number[][]} A - first matrix
 * @param {number[][]} B - second matrix
 * @param firstMatrixSlice - first matrix slice options
 * @param secondMatrixSlice - second matrix slice options
 * @param {number} size - slice size
 *
 * @returns {number[][]} product of `A` and `B` slices.
 */
function multiplyRecursively(
  A: number[][],
  B: number[][],
  firstMatrixSlice: MatrixSlicePositions,
  secondMatrixSlice: MatrixSlicePositions,
  size: number,
): number[][] {
  if (size === 1) {
    return [
      [
        A[firstMatrixSlice.rows][firstMatrixSlice.cols] *
          B[secondMatrixSlice.rows][secondMatrixSlice.cols],
      ],
    ];
  }

  const halfSize = size / 2;

  const C11 = addMatrices(
    multiplyRecursively(
      A,
      B,
      { rows: 0, cols: 0 },
      { rows: 0, cols: 0 },
      halfSize,
    ),
    multiplyRecursively(
      A,
      B,
      { rows: 0, cols: halfSize },
      { rows: halfSize, cols: 0 },
      halfSize,
    ),
  );
  const C12 = addMatrices(
    multiplyRecursively(
      A,
      B,
      { rows: 0, cols: 0 },
      { rows: 0, cols: halfSize },
      halfSize,
    ),
    multiplyRecursively(
      A,
      B,
      { rows: 0, cols: halfSize },
      { rows: halfSize, cols: halfSize },
      halfSize,
    ),
  );
  const C21 = addMatrices(
    multiplyRecursively(
      A,
      B,
      { rows: halfSize, cols: 0 },
      { rows: 0, cols: 0 },
      halfSize,
    ),
    multiplyRecursively(
      A,
      B,
      { rows: halfSize, cols: halfSize },
      { rows: halfSize, cols: 0 },
      halfSize,
    ),
  );
  const C22 = addMatrices(
    multiplyRecursively(
      A,
      B,
      { rows: halfSize, cols: 0 },
      { rows: 0, cols: halfSize },
      halfSize,
    ),
    multiplyRecursively(
      A,
      B,
      { rows: halfSize, cols: halfSize },
      { rows: halfSize, cols: halfSize },
      halfSize,
    ),
  );

  return combineFourMatrices(C11, C12, C21, C22);
}

/**
 * Combines four matrices in place.
 *
 * @param {number[][]} upperLeft - upper left matrix
 * @param {number[][]} upperRight - upper right matrix
 * @param {number[][]} lowerLeft - lower left matrix
 * @param {number[][]} lowerRight - lower right matrix
 *
 * @returns {number[][]} Combined matrix of `A`, `B`, `C` and `D`.
 */
export function combineFourMatrices(
  upperLeft: number[][],
  upperRight: number[][],
  lowerLeft: number[][],
  lowerRight: number[][],
): number[][] {
  const length = upperLeft.length;

  for (let i = 0; i < length; i++) {
    upperLeft[i + length] = [];
    for (let j = 0; j < length; j++) {
      upperLeft[i + length][j] = lowerLeft[i][j];
    }
  }

  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length; j++) {
      upperLeft[i][j + length] = upperRight[i][j];
    }
  }

  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length; j++) {
      upperLeft[i + length][j + length] = lowerRight[i][j];
    }
  }

  return upperLeft;
}

/**
 * Adds two matrices in place.
 *
 * @param {number[][]} A
 * @param {number[][]} B
 *
 * @returns {number[][]} Sum of `A` and `B`
 */

export function addMatrices(A: number[][], B: number[][]): number[][] {
  const length = A.length;

  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length; j++) {
      A[i][j] += B[i][j];
    }
  }
  return A;
}
