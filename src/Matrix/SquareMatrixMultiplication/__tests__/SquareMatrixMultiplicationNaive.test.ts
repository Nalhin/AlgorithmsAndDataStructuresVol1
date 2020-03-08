import { squareMatrixMultiplicationNaive } from '../SquareMatrixMultiplicationNaive';

describe('SquareMatrixMultiplicationNaive', () => {
  it('should multiply square matrices correctly', () => {
    const A = [
      [6, -2],
      [3, 7],
    ];
    const B = [
      [1, -2],
      [-3, 4],
    ];
    const expected = [
      [12, -20],
      [-18, 22],
    ];

    const result = squareMatrixMultiplicationNaive(A, B);

    expect(result).toEqual(expected);
  });
});
