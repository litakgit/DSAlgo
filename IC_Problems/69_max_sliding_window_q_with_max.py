
"""
Write a class for Q with max element.
"""

import collections

class QueueWithMax(object):
    def __init__(self):
        self.queue = collections.deque()
        self.max_queue = collections.deque()

    def insert(self, item):
        self.queue.append(item)

        while self.max_queue and self.max_queue[-1] < item:
            self.max_queue.pop()
        self.max_queue.append(item)

    def remove(self):
        if not self.queue:
            return None
        if self.max_queue[0] == self.queue[0]:
            self.max_queue.popleft()

        return self.queue.popleft()

    def get_max(self):
        return self.max_queue[0] if self.max_queue else None


def max_sliding_window_elem(seq, window_size):
    Q = QueueWithMax()
    for elem in seq[:window_size]:
        Q.insert(elem)
    print ("Queue : {}; Max Elem {}".format(Q.queue, Q.get_max()))

    for elem in seq[window_size:]:
        Q.remove()
        Q.insert(elem)
        print ("Queue : {}; Max Elem {}".format(Q.queue, Q.get_max()))


if __name__ == "__main__":
    Q = QueueWithMax()
    Q.insert(2)
    print (Q.get_max())
    Q.insert(7)
    Q.insert(7)
    print (Q.get_max())
    Q.insert(4)
    Q.remove()
    Q.remove()
    Q.remove()
    Q.remove()
    Q.remove()
    print (Q.get_max())
    Q.insert(5)
    print (Q.get_max())
    Q.insert(9)
    print (Q.get_max())
    print ("--- Testing Max Sliding Window Elem ---")
    max_sliding_window_elem([10,2,3,40,15,26,17,38,29], 3)
    max_sliding_window_elem([29], 3)
