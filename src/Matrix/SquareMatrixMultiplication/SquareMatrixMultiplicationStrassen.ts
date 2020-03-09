/**
 * Returns the product of two square matrices. Implemented with Strassen's algorithm.
 *
 * @param {number[][]} A - square matrix with the same size as `B`.
 * @param {number[][]} B - square matrix with the same size as `A`.
 *
 * @returns {number[][]} The product of `A` and `B`.
 */

export function squareMatrixMultiplicationStrassen(
  A: number[][],
  B: number[][],
) {
  return multiplyStrassen(A, B, {
    size: A.length,
  });
}

interface MatrixSlicePositions {
  rows: number;
  cols: number;
}

interface MatrixOptions {
  firstMatrixSlice?: MatrixSlicePositions;
  secondMatrixSlice?: MatrixSlicePositions;
}

interface StrassenOptions extends MatrixOptions {
  size: number;
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
function multiplyStrassen(
  A: number[][],
  B: number[][],
  {
    firstMatrixSlice = { rows: 0, cols: 0 },
    secondMatrixSlice = { rows: 0, cols: 0 },
    size,
  }: StrassenOptions,
): number[][] {
  if (size === 1) {
    return [
      [
        A[firstMatrixSlice.rows][firstMatrixSlice.rows] *
          B[secondMatrixSlice.rows][secondMatrixSlice.cols],
      ],
    ];
  }

  const halfSize = size / 2;

  const s1 = subtractMatrices(B, B, {
    firstMatrixSlice: { rows: 0, cols: halfSize },
    secondMatrixSlice: { rows: halfSize, cols: halfSize },
    size: halfSize,
  });
  const s2 = addMatrices(A, A, {
    firstMatrixSlice: { rows: 0, cols: 0 },
    secondMatrixSlice: { rows: 0, cols: halfSize },
    size: halfSize,
  });
  const s3 = addMatrices(A, A, {
    firstMatrixSlice: { rows: halfSize, cols: 0 },
    secondMatrixSlice: { rows: halfSize, cols: halfSize },
    size: halfSize,
  });

  const s4 = subtractMatrices(B, B, {
    firstMatrixSlice: { rows: halfSize, cols: 0 },
    secondMatrixSlice: { rows: 0, cols: 0 },
    size: halfSize,
  });
  const s5 = addMatrices(A, A, {
    firstMatrixSlice: { rows: 0, cols: 0 },
    secondMatrixSlice: { rows: halfSize, cols: halfSize },
    size: halfSize,
  });
  const s6 = addMatrices(B, B, {
    firstMatrixSlice: { rows: 0, cols: 0 },
    secondMatrixSlice: { rows: halfSize, cols: halfSize },
    size: halfSize,
  });
  const s7 = subtractMatrices(A, A, {
    firstMatrixSlice: { rows: 0, cols: halfSize },
    secondMatrixSlice: { rows: halfSize, cols: halfSize },
    size: halfSize,
  });
  const s8 = addMatrices(B, B, {
    firstMatrixSlice: { rows: halfSize, cols: 0 },
    secondMatrixSlice: { rows: halfSize, cols: halfSize },
    size: halfSize,
  });
  const s9 = subtractMatrices(A, A, {
    firstMatrixSlice: { rows: 0, cols: 0 },
    secondMatrixSlice: { rows: halfSize, cols: 0 },
    size: halfSize,
  });
  const s10 = addMatrices(B, B, {
    firstMatrixSlice: { rows: 0, cols: 0 },
    secondMatrixSlice: { rows: 0, cols: halfSize },
    size: halfSize,
  });

  const P1 = multiplyStrassen(A, s1, {
    firstMatrixSlice: { rows: 0, cols: 0 },
    size: halfSize,
  });
  const P2 = multiplyStrassen(s2, B, {
    secondMatrixSlice: { rows: halfSize, cols: halfSize },
    size: halfSize,
  });
  const P3 = multiplyStrassen(s3, B, {
    secondMatrixSlice: { rows: 0, cols: 0 },
    size: halfSize,
  });
  const P4 = multiplyStrassen(A, s4, {
    firstMatrixSlice: { rows: halfSize, cols: halfSize },
    size: halfSize,
  });
  const P5 = multiplyStrassen(s5, s6, {
    size: halfSize,
  });
  const P6 = multiplyStrassen(s7, s8, {
    size: halfSize,
  });
  const P7 = multiplyStrassen(s9, s10, { size: halfSize });

  const C11 = addMatrices(subtractMatrices(P4, P2), addMatrices(P5, P6));
  const C12 = addMatrices(P1, P2);
  const C21 = addMatrices(P3, P4);
  const C22 = subtractMatrices(addMatrices(P5, P1), addMatrices(P3, P7));

  return combineFourMatrices(C11, C12, C21, C22);
}

interface MatrixOperationOptions extends MatrixOptions {
  size: number;
}

/**
 * Immutably adds two matrices.
 *
 * @param {number[][]} A - first matrix
 * @param {number[][]} B - second matrix
 * @param {?MatrixOperationOptions} firstMatrixSlice - first matrix slice options
 * @param {?MatrixOperationOptions} secondMatrixSlice - second matrix slice options
 * @param {?number} size - slice size
 *
 * @returns {number[][]} sum of `A` and `B`.
 */
export function addMatrices(
  A: number[][],
  B: number[][],
  {
    firstMatrixSlice = { rows: 0, cols: 0 },
    secondMatrixSlice = { rows: 0, cols: 0 },
    size = A.length,
  } = {} as MatrixOperationOptions,
): number[][] {
  const C = [];

  for (let i = 0; i < size; i++) {
    C[i] = [];
    for (let j = 0; j < size; j++) {
      C[i][j] =
        A[i + firstMatrixSlice.rows][j + firstMatrixSlice.cols] +
        B[i + secondMatrixSlice.rows][j + secondMatrixSlice.cols];
    }
  }
  return C;
}

/**
 * Immutably subtracts two matrices.
 *
 * @param {number[][]} A - first Matrix
 * @param {number[][]} B - second matrix
 * @param {?MatrixOperationOptions} firstMatrixSlice - first matrix slice options
 * @param {?MatrixOperationOptions} secondMatrixSlice - second matrix slice options
 * @param {?number} size - slice size
 *
 * @returns {number[][]} Difference of `A` and `B`.
 */
export function subtractMatrices(
  A: number[][],
  B: number[][],
  {
    firstMatrixSlice = { rows: 0, cols: 0 },
    secondMatrixSlice = { rows: 0, cols: 0 },
    size = A.length,
  } = {} as MatrixOperationOptions,
): number[][] {
  const C = [];
  for (let i = 0; i < size; i++) {
    C[i] = [];
    for (let j = 0; j < size; j++) {
      C[i][j] =
        A[i + firstMatrixSlice.rows][j + firstMatrixSlice.cols] -
        B[i + secondMatrixSlice.rows][j + secondMatrixSlice.cols];
    }
  }
  return C;
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
