
def peak_elem(A):
    left, right = 0, len(A) - 1

    while left <= right:
        mid   = left + ((right-left)>>1)

        """
        Here we are handling the corner cases.
        """
        low  = A[mid-1] if mid > 0 else float('-inf')
        high = A[mid+1] if mid < len(A)-1 else float('-inf')

        if low < A[mid] < high:
            left = mid+1
        elif low > A[mid] > high:
            right = mid-1
        elif low > A[mid] and A[mid] < high:
            right = mid-1
        else:
            return A[mid]


if __name__ == "__main__":
    print (peak_elem([1,2,3,4,-1]))
