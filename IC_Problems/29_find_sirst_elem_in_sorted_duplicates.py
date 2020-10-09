

def get_first_elem_in_sorted_array(A, k):
    left, right = 0, len(A) - 1
    pos_found = float('inf')

    # Check you are covering all the elements here.
    # right and left is getting updated with the next/prev elements.
    while left <= right:
        mid = left + ((right - left) >> 1)
        if A[mid] == k:
            pos_found = min(pos_found, mid)
            right = mid - 1
        elif A[mid] > k:
            right = mid - 1
        else: # A[mid] < k
            left = mid + 1

    return pos_found if pos_found != float('inf') else -1


if __name__ == "__main__":
    A = [1,1,2,3,4,4,6,7,7,7,7,7]
    k = 7
    print (get_first_elem_in_sorted_array(A, k))
