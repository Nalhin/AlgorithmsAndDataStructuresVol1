import { maximumSubarrayDivideAndConquer } from '../MaximumSubarrayDivideAndConquer';

describe('MaximumSubarray Divide and Conquer', function () {
  it('should find maximum subarray', function () {
    const data = [1, -2, 3, 10, -5, 14];
    const expected = [3, 10, -5, 14];

    const result = maximumSubarrayDivideAndConquer(data);

    expect(result).toEqual(expected);
  });
});
