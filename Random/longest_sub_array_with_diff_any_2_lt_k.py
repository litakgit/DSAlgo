
# A = [3, 5, 4, 6, 1, 7, 8, 2, 5]
# k = 3

import collections

def get_sub_array_any_2_diff_less_than(A, k):
    def add_elem_in_min_max_qs(elem):
        while min_q and min_q[-1] > elem:
            min_q.pop()
        min_q.append(elem)

        while max_q and max_q[-1] < elem:
            max_q.pop()
        max_q.append(elem)

    def delete_elem_from_min_max_qs(elem):
        if min_q[0] == elem:
            min_q.popleft()
        if max_q[0] == elem:
            max_q.popleft()


    min_q = collections.deque()
    max_q = collections.deque()
    largest_sub_array = (0, (-1,-1))
    start = 0

    for end, elem in enumerate(A):
        add_elem_in_min_max_qs(elem)
        while max_q[0] - min_q[0] >= k:
            largest_sub_array = max(largest_sub_array, (end-start,(start, end-1)), key=lambda x : x[0])
            delete_elem_from_min_max_qs(A[start])
            start += 1
    largest_sub_array = max(largest_sub_array, (end-start+1,(start, end)), key=lambda x : x[0])

    return largest_sub_array

if __name__ == "__main__":
    A = [3, 5, 4, 6, 5, 7, 8, 6, 7 ]
    k = 3

    print (get_sub_array_any_2_diff_less_than(A, k))

