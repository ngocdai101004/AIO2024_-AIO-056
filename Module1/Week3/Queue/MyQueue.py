
class MyQueue:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.queue = []
        self.rear_pointer = -1

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.queue[0]
        del self.queue[0]
        self.rear_pointer -= 1
        return value

    def enqueue(self, value):
        if self.is_full():
            return False
        self.rear_pointer += 1
        self.queue.append(value)
        return True

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]


if __name__ == "__main__":
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.is_full())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.is_empty())
