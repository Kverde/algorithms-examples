import builtins
import unittest


def find(lst, element):
    for i, item in enumerate(lst):
        if item == element:
            return i

    return -1


def min(lst):
    if len(lst) == 0:
        raise ValueError('min() arg is an empty sequence')

    m = lst[0]
    for i, item in enumerate(lst[1:]):
        m = builtins.min(item, m)

    return m


class TestMin(unittest.TestCase):
    def test_empty(self):
        pass
        # TODO

    def test_correct(self):
        result = min([4, 7, 3, 8])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
