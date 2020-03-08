/**
 * Returns the product of two square matrices. Calculated with recursive algorithm.
 *
 * @param {number[][]} A - Matrix.
 * @param {number[][]} B - Matrix.
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

interface MatrixRowsAndCols {
  rows: number;
  cols: number;
}

function multiplyRecursively(
  A: number[][],
  B: number[][],
  aRowsAndCols: MatrixRowsAndCols,
  bRowsAndCols: MatrixRowsAndCols,
  size: number,
): number[][] {
  if (size === 1) {
    const C = [[]];

    C[0][0] =
      A[aRowsAndCols.rows][aRowsAndCols.cols] *
      B[bRowsAndCols.rows][bRowsAndCols.cols];
    return C;
  }

  const halfSize = size / 2;

  const c11 = addMatrices(
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
  const c12 = addMatrices(
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
  const c21 = addMatrices(
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
  const c22 = addMatrices(
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

  return combineFourMatrices(c11, c12, c21, c22);
}

export function combineFourMatrices(
  upperLeft: number[][],
  upperRight: number[][],
  lowerLeft: number[][],
  lowerRight: number[][],
): number[][] {
  const length = upperLeft.length;
  const C = [];

  for (let i = 0; i < length; i++) {
    C[i] = [];
    for (let j = 0; j < length; j++) {
      C[i][j] = upperLeft[i][j];
    }
  }

  for (let i = 0; i < length; i++) {
    C[i + length] = [];
    for (let j = 0; j < length; j++) {
      C[i + length][j] = lowerLeft[i][j];
    }
  }

  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length; j++) {
      C[i][j + length] = upperRight[i][j];
    }
  }

  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length; j++) {
      C[i + length][j + length] = lowerRight[i][j];
    }
  }

  return C;
}

export function addMatrices(A: number[][], B: number[][]): number[][] {
  const length = A.length;
  const C = [[]];

  for (let i = 0; i < length; i++) {
    C[i] = [];
    for (let j = 0; j < length; j++) {
      C[i][j] = A[i][j] + B[i][j];
    }
  }
  return C;
}
