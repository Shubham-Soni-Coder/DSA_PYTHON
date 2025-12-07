class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            return "overflow"
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            return "empty"
        else:
            data = self.stack[self.top]
            self.top -= 1
            return data

    def traverse(self):
        for i in range(self.top + 1):
            print(self.stack[i], end=" ")
