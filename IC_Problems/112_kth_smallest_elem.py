
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
        # randrange throws exception is start==end
        random_pivot = random.randrange(start, end)
        pivot = get_pivot_after_partition(A, start, end, A[random_pivot])

        if pivot == k:
            return A[pivot]
        elif pivot > k:
            start, end = start, pivot
        else:
            start, end = pivot+1, end
    return -1


if __name__ == "__main__":
    A = [3,5,9,10,12,2,7,8]
    k = 5
    A = [5,7,7,5]
    k = 1
    print (get_kth_smallest_elem(A, k))
