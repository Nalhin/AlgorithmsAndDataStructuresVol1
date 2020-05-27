from src.Problems.MaximumSubarray.maximum_substring_naive import (
    maximum_subarray_naive,
)


class TestMaximumSubarrayNaive:
    def test_returns_maximum_subarray(self):
        data = [1, -2, 3, 10, -5, 14]
        expected = [3, 10, -5, 14]

        result = maximum_subarray_naive(data)

        assert result == expected
