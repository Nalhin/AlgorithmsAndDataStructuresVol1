/**
 * Returns the product of two square matrices. Calculated with recursive algorithm.
 *
 * @param {number[][]} A - Matrix.
 * @param {number[][]} B - Matrix.
 * @returns {number[][]} The product of `A` and `B`.
 */

export function squareMatrixMultiplicationStrassen(
  A: number[][],
  B: number[][],
) {
  return multiplyStrassen(
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

function multiplyStrassen(
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

  const s1 = subtractMatricesWithBounds(
    B,
    B,
    { rows: 0, cols: halfSize },
    { rows: halfSize, cols: halfSize },
    halfSize,
  );
  const s2 = addMatricesWithBounds(
    A,
    A,
    { rows: 0, cols: 0 },
    { rows: 0, cols: halfSize },
    halfSize,
  );
  const s3 = addMatricesWithBounds(
    A,
    A,
    { rows: halfSize, cols: 0 },
    { rows: halfSize, cols: halfSize },
    halfSize,
  );

  const s4 = subtractMatricesWithBounds(
    B,
    B,
    { rows: halfSize, cols: 0 },
    { rows: 0, cols: 0 },
    halfSize,
  );
  const s5 = addMatricesWithBounds(
    A,
    A,
    { rows: 0, cols: 0 },
    { rows: halfSize, cols: halfSize },
    halfSize,
  );
  const s6 = addMatricesWithBounds(
    B,
    B,
    { rows: 0, cols: 0 },
    { rows: halfSize, cols: halfSize },
    halfSize,
  );
  const s7 = subtractMatricesWithBounds(
    A,
    A,
    { rows: 0, cols: halfSize },
    { rows: halfSize, cols: halfSize },
    halfSize,
  );
  const s8 = addMatricesWithBounds(
    B,
    B,
    { rows: halfSize, cols: 0 },
    { rows: halfSize, cols: halfSize },
    halfSize,
  );
  const s9 = subtractMatricesWithBounds(
    A,
    A,
    { rows: 0, cols: 0 },
    { rows: halfSize, cols: 0 },
    halfSize,
  );
  const s10 = addMatricesWithBounds(
    B,
    B,
    { rows: 0, cols: 0 },
    { rows: 0, cols: halfSize },
    halfSize,
  );

  const p1 = multiplyStrassen(
    A,
    s1,
    { rows: 0, cols: 0 },
    { rows: 0, cols: 0 },
    halfSize,
  );
  const p2 = multiplyStrassen(
    s2,
    B,
    { rows: 0, cols: 0 },
    { rows: halfSize, cols: halfSize },
    halfSize,
  );
  const p3 = multiplyStrassen(
    s3,
    B,
    { rows: 0, cols: 0 },
    { rows: 0, cols: 0 },
    halfSize,
  );
  const p4 = multiplyStrassen(
    A,
    s4,
    { rows: halfSize, cols: halfSize },
    { rows: 0, cols: 0 },
    halfSize,
  );
  const p5 = multiplyStrassen(
    s5,
    s6,
    { rows: 0, cols: 0 },
    { rows: 0, cols: 0 },
    halfSize,
  );
  const p6 = multiplyStrassen(
    s7,
    s8,
    { rows: 0, cols: 0 },
    { rows: 0, cols: 0 },
    halfSize,
  );
  const p7 = multiplyStrassen(
    s9,
    s10,
    { rows: 0, cols: 0 },
    { rows: 0, cols: 0 },
    halfSize,
  );

  const c11 = addMatrices(subtractMatrices(p4, p2), addMatrices(p5, p6));
  const c12 = addMatrices(p1, p2);
  const c21 = addMatrices(p3, p4);
  const c22 = subtractMatrices(addMatrices(p5, p1), addMatrices(p3, p7));

  return combineFourMatrices(c11, c12, c21, c22);
}

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

export function addMatricesWithBounds(
  A: number[][],
  B: number[][],
  aRowsAndCols: MatrixRowsAndCols,
  bRowsAndCols: MatrixRowsAndCols,
  size: number,
): number[][] {
  const C = [];

  for (let i = 0; i < size; i++) {
    C[i] = [];
    for (let j = 0; j < size; j++) {
      C[i][j] =
        A[i + aRowsAndCols.rows][j + aRowsAndCols.cols] +
        B[i + bRowsAndCols.rows][j + bRowsAndCols.cols];
    }
  }
  return C;
}

export function subtractMatricesWithBounds(
  A: number[][],
  B: number[][],
  aRowsAndCols: MatrixRowsAndCols,
  bRowsAndCols: MatrixRowsAndCols,
  size: number,
): number[][] {
  const C = [];
  for (let i = 0; i < size; i++) {
    C[i] = [];
    for (let j = 0; j < size; j++) {
      C[i][j] =
        A[i + aRowsAndCols.rows][j + aRowsAndCols.cols] -
        B[i + bRowsAndCols.rows][j + bRowsAndCols.cols];
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

export function subtractMatrices(A: number[][], B: number[][]): number[][] {
  const length = A.length;
  const C = [[]];

  for (let i = 0; i < length; i++) {
    C[i] = [];
    for (let j = 0; j < length; j++) {
      C[i][j] = A[i][j] - B[i][j];
    }
  }
  return C;
}
