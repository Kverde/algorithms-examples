import unittest


def binary_search(lst, item):
    """
    Функция возвощает индекс элемента item в списке lst
    или -1 если элемент не найден.
    """
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = first + (last - first) // 2

        if lst[mid] == item:
            return mid

        if lst[mid] < item:
            first = mid + 1
        else:
            last = mid - 1

    return -1


class TestBinarySearch(unittest.TestCase):
    def test_empty_list(self):
        result = binary_search([], 4)
        self.assertEqual(result, -1)

    def test_list_with_one_item(self):
        result = binary_search([4], 4)
        self.assertEqual(result, 0)

        result = binary_search([6], 4)
        self.assertEqual(result, -1)

    def test_list_with_two_items(self):
        result = binary_search([4, 6], 3)
        self.assertEqual(result, -1)

        result = binary_search([4, 6], 4)
        self.assertEqual(result, 0)

        result = binary_search([4, 6], 6)
        self.assertEqual(result, 1)

    def test_list_with_five_items(self):
        result = binary_search([1, 2, 3, 4, 5], 0)
        self.assertEqual(result, -1)

        result = binary_search([1, 2, 3, 4, 5], 7)
        self.assertEqual(result, -1)

        result = binary_search([1, 2, 3, 4, 5], 1)
        self.assertEqual(result, 0)

        result = binary_search([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, 1)

        result = binary_search([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, 2)

        result = binary_search([1, 2, 3, 4, 5], 4)
        self.assertEqual(result, 3)

        result = binary_search([1, 2, 3, 4, 5], 5)
        self.assertEqual(result, 4)

    def test_list_with_six_items(self):
        result = binary_search([1, 2, 3, 4, 5, 6], 0)
        self.assertEqual(result, -1)

        result = binary_search([1, 2, 3, 4, 5, 6], 7)
        self.assertEqual(result, -1)

        result = binary_search([1, 2, 3, 4, 5, 6], 1)
        self.assertEqual(result, 0)

        result = binary_search([1, 2, 3, 4, 5, 6], 2)
        self.assertEqual(result, 1)

        result = binary_search([1, 2, 3, 4, 5, 6], 3)
        self.assertEqual(result, 2)

        result = binary_search([1, 2, 3, 4, 5, 6], 4)
        self.assertEqual(result, 3)

        result = binary_search([1, 2, 3, 4, 5, 6], 5)
        self.assertEqual(result, 4)

        result = binary_search([1, 2, 3, 4, 5, 6], 6)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
