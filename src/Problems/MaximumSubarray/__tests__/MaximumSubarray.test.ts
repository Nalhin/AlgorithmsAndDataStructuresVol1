import { maximumSubarrayDivideAndConquer } from '../MaximumSubarrayDivideAndConquer';

describe('MaximumSubarray', function() {
  it('should find maximum subarray', function() {
    const data = [1, -2, 3, 10, -5, 14];
    const expected = [3, 10, -5, 14];

    const result = maximumSubarrayDivideAndConquer(data);

    expect(result.end).toEqual(5);
    expect(result.start).toEqual(2);
    expect(result.sum).toEqual(expected.reduce((a, b) => a + b, 0))
  });
});