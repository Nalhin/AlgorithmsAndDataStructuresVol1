from src.OrderStatistics.RandomizedSelect.randomized_select import randomized_select


class TestRandomizedSelect:
    def test_randomized_select(self):
        array = [1, 3, 4, 1, 7, 8, 9]
        expected = 7

        result = randomized_select(array, 5)

        assert result == expected
