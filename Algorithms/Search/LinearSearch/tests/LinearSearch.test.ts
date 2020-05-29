import { linearSearch } from '../LinearSearch';

describe('Linear search', () => {
  it('should find index of given value in array', () => {
    const array = [1, 3, 2, 4, 5, 6, 2, 1, 9];
    const expectedValue = 3;
    const valueToFind = 4;

    const value = linearSearch(array, valueToFind);

    expect(value).toEqual(expectedValue);
  });
  it('should return null if value is missing', () => {
    const array = [1, 3, 2, 4, 5, 6, 2, 1, 9];

    const value = linearSearch(array, 10);

    expect(value).toBeFalsy();
  });
});
