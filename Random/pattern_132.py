
# l = [4, 3, 9, 2, 1]
# l = [4, 3, 9, 6, 1]
# l = [4, 8, 6, 9, 2, 5, 3]
# i < j < k such that A[i] < A[k] < A[j]

def get_132_pattern(A):
    stack = []
    max_popped_elem = (float('-inf'), None)
    last_popped_elem = (float('-inf'), None)
    for pos, elem in enumerate(A[::-1]):
        if elem < max_popped_elem[0]:
            # pos is from backside.
            return (elem, len(A)-1-pos), max_popped_elem, stack[-1]
        # stack elem is tuple.
        while stack and stack[-1][0] < elem: # TODO : check the <= condition.
            last_popped_elem = stack.pop()
        # getting max tuple from tuples.
        max_popped_elem = max(max_popped_elem, last_popped_elem, key=lambda x: x[0])
        stack.append((elem, len(A)-1-pos))
    return (-1,-1,-1)

if __name__ == "__main__":
    A = [4, 8, 3, 9, 4, 5, 3]
    A = [1,5,3,4,5,6]
    print (A)
    print (get_132_pattern(A))
