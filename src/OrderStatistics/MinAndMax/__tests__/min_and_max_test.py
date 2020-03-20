from src.OrderStatistics.MinAndMax.min_and_max import min_and_max


class TestMinAndMax:
    def test_min_and_max_even_length(self):
        array = [1, 3, 4, 1, 5, 7]
        expected = (1, 7)

        result = min_and_max(array)

        assert result == expected

    def test_min_and_max_odd_length(self):
        array = [1, 3, 4, 1, 1, 5, 7]
        expected = (1, 7)

        result = min_and_max(array)

        assert result == expected
