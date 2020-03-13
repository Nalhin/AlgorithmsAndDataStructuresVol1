import { randomizeInPlace } from '../RandomizeInPlace';

describe('RandomizeInPlace', function() {
  it('should return array with the same length and values', function() {
    const array = [1, 2, 3, 4, 5];
    const result = [...array];

    randomizeInPlace(result);

    expect(result).toHaveLength(array.length);
    expect(result.sort()).toEqual(array.sort());
  });
});
