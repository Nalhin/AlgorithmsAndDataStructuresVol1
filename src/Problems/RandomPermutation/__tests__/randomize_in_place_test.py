from src.Problems.RandomPermutation.randomize_in_place import randomize_in_place


class TestRandomizeInPlace:
    def test_same_elements_and_length(self):
        array = [1, 2, 3, 4, 5]
        result = array.copy()

        randomize_in_place(result)

        assert len(result) == len(array)
        assert result.sort() == array.sort()
