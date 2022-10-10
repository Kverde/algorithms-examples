import pytest

from examples.case_default_exception import day_of_week1, day_of_week2, day_of_week3, day_of_week4, day_of_week5


@pytest.mark.parametrize("day_of_week", [day_of_week1, day_of_week2, day_of_week3, day_of_week4, day_of_week5])
class TestDayOfWeekCorrect:
    def test_day_of_week(self, day_of_week):
        assert day_of_week(0) == 'Понедельник'
        assert day_of_week(1) == 'Вторник'
        assert day_of_week(2) == 'Среда'
        assert day_of_week(3) == 'Четверг'
        assert day_of_week(4) == 'Пятница'
        assert day_of_week(5) == 'Суббота'
        assert day_of_week(6) == 'Воскресенье'


class TestDayOfWeekWrong:
    def test_day_of_week1(self):
        with pytest.raises(UnboundLocalError):
            day_of_week1(23)

    def test_day_of_week2(self):
        assert day_of_week2(23) == 'Неверный день недели'

    def test_day_of_week3(self):
        with pytest.raises(ValueError):
            day_of_week3(22)

    def test_day_of_week4(self):
        with pytest.raises(ValueError):
            day_of_week4(22)

    def test_day_of_week5(self):
        with pytest.raises(ValueError):
            day_of_week5(22)
