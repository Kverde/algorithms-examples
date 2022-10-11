import pytest

from source.selection_sort import selection_sort01
from source.quicksort import quicksort


@pytest.mark.parametrize("sort", [selection_sort01, quicksort])
class TestSort():
    def test_empty(self, sort):
        assert sort([]) == []

    def test_one_elements(self, sort):
        assert sort([4]) == [4]

    def test_two_elements(self, sort):
        assert sort([3, 8]) == [3, 8]
        assert sort([22, 11]) == [11, 22]

    def test_sort(self, sort):
        assert sort([44, 7, 12, 1, 8]) == [1, 7, 8, 12, 44]
