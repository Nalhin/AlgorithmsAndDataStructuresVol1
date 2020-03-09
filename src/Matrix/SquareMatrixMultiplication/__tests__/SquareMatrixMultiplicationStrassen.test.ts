import {
  addMatrices,
  combineFourMatrices,
  squareMatrixMultiplicationStrassen,
  subtractMatrices,
} from '../SquareMatrixMultiplicationStrassen';

describe('SquareMatrixMultiplicationStrassen', () => {
  describe('addMatrices', () => {
    it('should add matrices', () => {
      const A = [
        [6, -2],
        [3, 7],
      ];
      const B = [
        [1, 2],
        [3, 4],
      ];
      const expected = [
        [7, 0],
        [6, 11],
      ];

      const result = addMatrices(A, B);

      expect(result).toEqual(expected);
    });
  });

  describe('subtractMatrices', () => {
    it('should substract matrices', () => {
      const A = [
        [6, -2],
        [3, 7],
      ];
      const B = [
        [1, 2],
        [3, 4],
      ];
      const expected = [
        [5, -4],
        [0, 3],
      ];

      const result = subtractMatrices(A, B);

      expect(result).toEqual(expected);
    });
  });

  describe('combineFourMatrices', () => {
    it('should combine four matrices', () => {
      const A = [
        [6, -2],
        [3, 7],
      ];
      const B = [
        [1, -2],
        [-3, 4],
      ];
      const C = [
        [1, 2],
        [3, 4],
      ];
      const D = [
        [5, 6],
        [7, 8],
      ];
      const expected = [
        [6, -2, 1, -2],
        [3, 7, -3, 4],
        [1, 2, 5, 6],
        [3, 4, 7, 8],
      ];

      const result = combineFourMatrices(A, B, C, D);

      expect(result).toEqual(expected);
    });
  });

  describe('squareMatrixMultiplicationStrassen', () => {
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

      const result = squareMatrixMultiplicationStrassen(A, B);

      expect(result).toEqual(expected);
    });
  });
});
