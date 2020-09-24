import collections

class QueueWithMax(object):
    def __init__(self):
        self.queue = collections.deque()
        self.max_queue = collections.deque()

    def insert(self, elem):
        while self.queue and self.queue[-1][1] == elem[1]:
            self.queue.pop()
        self.queue.append(elem)

        while self.max_queue and self.max_queue[-1][1] == elem[1]:
            self.max_queue.pop()
        while self.max_queue and self.max_queue[-1][0] <= elem[0]:
            self.max_queue.pop()
        self.max_queue.append(elem)

    def remove(self):
        if not self.queue:
            return None
        popped_elem = self.queue.popleft()
        # Checked the popped_elem in max_queue.
        if popped_elem[0] == self.max_queue[0][0]:
            self.max_queue.popleft()

    def get_max_elem(self):
        return self.max_queue[0]

    def get_queue_len(self):
        return len(self.queue)

def get_max_stock_price_in_last_n_days(A, k):
    res = []
    Q = QueueWithMax()

    for elem in A:
        Q.insert(elem)
        if Q.get_queue_len() > k:
            Q.remove()
        res.append(Q.get_max_elem())

    return res

if __name__ == "__main__":
    A = [(32,1), (43,1), (39,1), (24,2), (41,3), (45,3), (21,4), (38,5), (37,6), (34,7), (32,8)]
    print (A)
    print (get_max_stock_price_in_last_n_days(A, 3))
