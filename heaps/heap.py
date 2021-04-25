from helpers import *


class MaxHeap:
    def __init__(self):
        self.arr = None
        self.n = 0

    def insert(self, x):
        self.n += 1
        self.arr[self.n -1] = x
        fix_up(self.arr, self.n -1)

    def delete(self):
        swap(self.arr[0], self.arr[self.n -1])
        self.n -= 1
        fix_down(self.arr, self.n, 0)
        return self.arr[self.n]
