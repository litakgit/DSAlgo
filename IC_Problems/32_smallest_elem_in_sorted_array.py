"""
Lessons :
    - Right shift operator will need start and closing bracket.
    - Beauty is left and right calculation.
"""

def get_smallest_elm_in_sorted_array(A):
    left, right = 0, len(A)-1
    while left < right:
        mid = left + ((right - left) >> 1)
        if A[mid] < A[right]:
            right = mid
        elif A[mid] > A[right]:
            left = mid+1
    return A[left]

if __name__ == "__main__":
    A = [190, 200, 210, 222, 3, 32, 76, 121, 135]
    print (get_smallest_elm_in_sorted_array(A))
