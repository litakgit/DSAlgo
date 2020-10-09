

def get_min_in_rotated_sorted_array(A):
    left, right = 0, len(A) - 1

    while left < right:
        mid = left + ((right - left) >> 1)
        if A[mid] > A[right]:
            left = mid + 1
        elif A[mid] < A[right]:
            right = mid
        else:
            # This is required because elements can be duplicated.
            right_sum = sum(A[mid:right+1])
            if right_sum < (right+1-mid) * A[mid]:
                left = mid + 1
            else:
                right = mid

    return A[left]

if __name__ == "__main__":
    A = [4,5,6,6,6,6,1,2,2,2,2 ,2]
    A = [3,3,2,3]
    print (get_min_in_rotated_sorted_array(A))
