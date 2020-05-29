from Algorithms.Problems.MaximumSubarray.maximum_subarray_kadane import (
    maximum_subarray_kadane,
)


class TestMaximumSubarrayKadane:
    def test_returns_maximum_subarray(self):
        data = [1, -2, 3, 10, -5, 14]
        expected = [3, 10, -5, 14]

        result = maximum_subarray_kadane(data)

        assert result == expected
