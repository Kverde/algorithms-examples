import pytest

from source.linear_search import linear_search


class TestLinearSearch():
    def test_empty(self):
        assert linear_search([], 2) == -1

    def test_one(self):
        assert linear_search([2], 2) == 0

    def test_many(self):
        assert linear_search([1, 4, 3, 2], 3) == 2

    def test_not_found(self):
        assert linear_search([1, 1, 3, 8, 5], 7) == -1
