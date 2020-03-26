import { permutateBySorting } from '../PermutateBySorting';

describe('PermutateBySorting', () => {
  it('should return array with the same length and values', () => {
    const array = [1, 2, 3, 4, 5];

    const result = permutateBySorting(array);

    expect(result).toHaveLength(array.length);
    expect(result.sort()).toEqual(array.sort());
  });
});
