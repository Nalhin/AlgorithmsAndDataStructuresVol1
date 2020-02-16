import { linearSearch } from '../LinearSearch';

describe('Linear search', () => {
  it('should find index of given value in array', () => {
    const array = [1, 3, 2, 4, 5, 6, 2, 1];
    const expectedValue = 3;

    const value = linearSearch(array, 4);

    expect(value).toEqual(expectedValue);
  });
});
