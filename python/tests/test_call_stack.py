from examples.call_stack import calc_distance


class TestCalcDistance:
    def test_stack(self):
        assert calc_distance(2, 3, 5, 3) == 3
        assert calc_distance(7, 9, 7, 9) == 0
