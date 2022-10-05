import unittest

from selection_sort import selection_sort


class TestBinarySearch(unittest.TestCase):
    def test_empty(self):
        result = selection_sort([])
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
