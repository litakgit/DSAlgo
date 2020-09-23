
def get_index_to_place_val(A, val):
    # Return the right index if val matches,
    # Else return the index to properly place the elem.
    left, right = 0, len(A)-1
    probable_pos = len(A)
    while left <= right:
        mid = left + ((right-left) >> 1)
        if A[mid] == val:
            return mid
        elif A[mid] > val:
            probable_pos = min(probable_pos, mid)
            right =  mid-1
        else:
            left = mid+1
    return probable_pos


if __name__ == "__main__":
    A = [1, 3, 5, 7, 10]
    print (get_index_to_place_val(A, 7))
