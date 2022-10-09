import unittest

from selection_sort import selection_sort


class TestSort(unittest.TestCase):
    def test_empty(self):
        result = selection_sort([])
        self.assertEqual(result, [])

    def test_one_elements(self):
        result = selection_sort([4])
        self.assertEqual(result, [4])

    def test_two_elements(self):
        result = selection_sort([3, 8])
        self.assertEqual(result, [3, 8])

        result = selection_sort([22, 11])
        self.assertEqual(result, [11, 22])

    def test_sort(self):
        result = selection_sort([44, 7, 12, 1, 8])
        self.assertEqual(result, [1, 7, 8, 12, 44])


if __name__ == '__main__':
    unittest.main()
