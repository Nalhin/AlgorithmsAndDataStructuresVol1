from src.Problems.RandomPermutation.permutate_by_sorting import permutate_by_sorting


class TestPermutateBySorting:
    def test_same_elements_and_length(self):
        array = [1, 2, 3, 4, 5]

        result = permutate_by_sorting(array)

        assert len(result) == len(array)
        assert result.sort() == array.sort()
