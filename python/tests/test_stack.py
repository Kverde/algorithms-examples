import pytest

from source.stack import StackList, StackDeque, EmptyStackError


@pytest.mark.parametrize("stack_class", [StackList, StackDeque])
class TestStack:
    @pytest.fixture()
    def stack(self, stack_class):
        return stack_class()

    def test_stack(self, stack):
        stack.push(5)
        stack.push(9)
        stack.push(3)

        assert stack.pop() == 3
        assert stack.pop() == 9
        assert stack.pop() == 5

    def test_top(self, stack):
        stack.push(5)
        assert stack.top() == 5
        assert stack.pop() == 5

        with pytest.raises(EmptyStackError):
            stack.top()

    def test_pop_empty(self, stack):
        with pytest.raises(EmptyStackError):
            stack.pop()

    def test_len(self, stack):
        assert stack.len() == 0

        stack.push(9)
        assert stack.len() == 1

        stack.push(3)
        assert stack.len() == 2

        stack.pop()
        assert stack.len() == 1

        stack.pop()
        assert stack.len() == 0
