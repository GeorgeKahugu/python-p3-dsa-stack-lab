
class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise OverflowError("Stack limit reached")

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        try:
            return self.items[::-1].index(target)
        except ValueError:
            return -1
