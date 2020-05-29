from Algorithms.Search.LinearSearch.linear_search import linear_search


class TestLinearSearch:
    def test_element_found(self):
        array = [1, 3, 2, 4, 4, 5]
        expected = 3

        index = linear_search(array, 4)

        assert index == expected

    def test_element_not_found(self):
        array = [1, 3, 2, 4, 4, 5]
        expected = None

        index = linear_search(array, 10)

        assert index == expected
