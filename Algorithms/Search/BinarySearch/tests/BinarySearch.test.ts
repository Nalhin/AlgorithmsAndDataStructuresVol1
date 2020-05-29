import { binarySearch } from '../BinarySearch';

describe('Binary search', () => {
  it('should find index of given value in array', () => {
    const array = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    const valueToFind = 4;
    const expectedPosition = 3;

    const value = binarySearch(array, valueToFind);

    expect(value).toEqual(expectedPosition);
  });
  it('should return null if value is missing', () => {
    const array = [1, 3, 2, 4, 5, 6, 2, 1, 9].sort();

    const value = binarySearch(array, 10);

    expect(value).toBeFalsy();
  });
});
