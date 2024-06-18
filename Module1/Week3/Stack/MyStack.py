
class MyStack:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.stack = []
        self.top_pointer = -1

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if self.is_empty():
            return None
        value = self.stack[self.top_pointer]
        del self.stack[self.top_pointer]
        self.top_pointer -= 1
        return value

    def push(self, value):
        if self.is_full():
            return False
        self.top_pointer += 1
        self.stack.append(value)
        return True

    def top(self):
        if self.is_empty():
            return None
        return self.stack[self.top_pointer]


if __name__ == "__main__":
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    stack1.push(2)
    print(stack1.is_full())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.is_empty())
