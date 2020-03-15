import { maximumSubarrayKadane } from '../MaximumSubarrayKadane';

describe('MaximumSubarray Linear', () => {
  it('should find maximum subarray', () => {
    const data = [1, -2, 3, 10, -5, 14];
    const expected = [3, 10, -5, 14];

    const result = maximumSubarrayKadane(data);

    expect(result).toEqual(expected);
  });
});
