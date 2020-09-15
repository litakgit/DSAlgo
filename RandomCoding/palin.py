def get_palindromic_decomposition(A):
    def helper(buf, pos): # [],0; 
        if pos == len(A): # 4;
            res.append(buf.copy())
            return
        for i in range(pos+1, len(A)+1):# 1-5;2-5;3-5;4-5
            prefix = A[pos:i]#0-1;
            if prefix == prefix[::-1]:
                buf.append(prefix)
                helper(buf, i)
                buf.pop()
    buf = []
    res = []
    helper(buf, 0)
    return res

def get_palindromic_decomposition2(A):
    def helper(buf, buf_index, pos):
        #import pdb; pdb.set_trace()
        if pos == len(A):
            res.append(buf[:buf_index].copy())
            print (buf)
            return
        for i in range(pos+1, len(A)+1):
            prefix = A[pos:i]#0-1;
            if prefix == prefix[::-1]:
                buf[buf_index] = prefix
                helper(buf, buf_index+1, i)
    buf = [-1] * len(A)
    res = []
    helper(buf, 0, 0)
    return res

def get_palindromic_decomposition1(A):

    def helper(buf, pos):
        if pos == len(A):
            res.append(buf.copy())
            return
        for i in range(pos+1, len(A)+1):
            prefix = A[pos:i]
            if prefix == prefix[::-1]:
                helper(buf+[prefix], i)
    res = []
    helper([], 0)
    return res

if __name__ == "__main__":
    res = get_palindromic_decomposition1("0204451881")
    print (res)
    res = get_palindromic_decomposition("0220")
    print (res)
    res = get_palindromic_decomposition2("0204451881")
    print (res)
