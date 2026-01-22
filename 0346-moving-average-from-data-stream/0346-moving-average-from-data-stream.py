from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.moving_sum = 0
        self.dequeue = deque([])

    def next(self, val: int) -> float:
        if len(self.dequeue)==self.size:
            popped = self.dequeue.popleft()
            self.moving_sum -= popped
        self.moving_sum += val
        self.dequeue.append(val)
        return self.moving_sum / (self.size if len(self.dequeue)==self.size else len(self.dequeue))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)