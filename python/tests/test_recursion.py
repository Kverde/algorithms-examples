import pytest

from examples.recursion import factorial01


@pytest.mark.parametrize("factorial", [factorial01])
class TestFactorial:
    def test_day_of_week(self, factorial):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
