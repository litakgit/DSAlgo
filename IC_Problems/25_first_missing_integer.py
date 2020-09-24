
def get_first_missing_elem(A):
    for i in range(len(A)):
        while A[i] >= 0 and A[i] < len(A) and A[A[i]] != A[i]:
            # print ("A: {} i:{} swap {} {}".format(A, i, A[i], A[A[i]]))
            # a, b = b, a won't work here !
            tmp = A[i]
            A[i] = A[A[i]]
            A[tmp] = tmp

    #return next((i for i, v in enumerate(A) if i != v), len(A))
    for i, v in enumerate(A):
        if i != v:
            return i
    return len(A)

if __name__ == "__main__":
    A = [1, 0, 10, 2, 31]
    print (get_first_missing_elem(A))
    #print (A)
