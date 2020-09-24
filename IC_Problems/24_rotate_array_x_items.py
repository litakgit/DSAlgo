
def rotate_item_by_x(A, k):
    def swap(S, start, end):
        while start < end:
            S[start], S[end] = S[end], S[start]
            start += 1
            end -= 1

    k = k % len(A)
    swap(A, 0, len(A)-1)
    swap(A, 0, k-1)
    swap(A, k, len(A)-1)
    return A

if __name__ == "__main__":
    A = [ 1, 5,2, 7, 3, 8]
    print (A)
    rotate_item_by_x(A, 9)
    print (A)
