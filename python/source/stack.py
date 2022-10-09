from collections import deque


class EmptyStackError(Exception):
    pass


class StackList():

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise EmptyStackError("pop from empty stack")

    def top(self):
        try:
            return self.stack[-1]
        except IndexError:
            raise EmptyStackError("top from empty stack")

    def len(self):
        return len(self.stack)


class StackDeque():

    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise EmptyStackError("pop from empty stack")

    def top(self):
        try:
            return self.stack[-1]
        except IndexError:
            raise EmptyStackError("top from empty stack")

    def len(self):
        return len(self.stack)
