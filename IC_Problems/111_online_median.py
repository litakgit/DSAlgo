
import heapq

def online_median(A):
    min_heap, max_heap = [], []
    res = []

    for x in A:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        median = (min_heap[0] if len(min_heap) > len(max_heap) else
                    (0.5 * (min_heap[0]-max_heap[0])))
        res.append(median)
    return res

if __name__ == "__main__":
    A = [1, 2,6,3,4,7]
    print (A)
    print (online_median(A))
