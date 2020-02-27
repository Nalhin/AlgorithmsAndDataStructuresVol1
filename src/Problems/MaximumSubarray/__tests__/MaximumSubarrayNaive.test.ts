import { maximumSubarrayNaive } from '../MaximumSubarrayNaive';

describe('MaximumSubarray Naive', function() {
  it('should find maximum subarray', function() {
    const data = [1, -2, 3, 10, -5, 14];
    const expected = [3, 10, -5, 14];

    const result = maximumSubarrayNaive(data);

    expect(result).toEqual(expected);
  });
});
