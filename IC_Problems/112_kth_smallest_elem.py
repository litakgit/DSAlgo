
import random

# In DNF, pivot is the value of the array element not the index!
def get_pivot_after_partition(A, start, end, rpivot):
    left_boundary, right_boundary = start, end-1
    i = left_boundary

    def swap(A, i, j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

    while i <= right_boundary:
        if A[i] > rpivot:
            swap (A, i, right_boundary)
            right_boundary -= 1
        elif A[i] < rpivot:
            swap(A, i, left_boundary)
            i += 1
            left_boundary += 1
        else:
            i += 1
    return left_boundary


def get_kth_smallest_elem(A, k):
    start, end = 0, len(A)
    while start < end:
        # randrange throws exception is start==end. So the above condition.
        # randrange generates random no from start to end-1.
        random_pivot = random.randrange(start, end)
        pivot = get_pivot_after_partition(A, start, end, A[random_pivot])

        if pivot == k:
            return A[pivot]
        elif pivot > k:
            # here end will be pivot because randrange will generate nos
            # from start to pivot-1. If we put end = pivot-1 then we are
            # going to loose pivot-1. And if pivot-1 is the right elem,
            # then wrong answer. 
            start, end = start, pivot
        else:
            # Here start will be pivot+1, and randrange will use this no.
            start, end = pivot+1, end
        #print (start, end)
    return -1


if __name__ == "__main__":
    A = [3,5,9,10,12,2,7,8]
    k = 5
    A = [5,7,7,5]
    k = 1
    print (get_kth_smallest_elem(A, k))
