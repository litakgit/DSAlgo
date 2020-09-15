
def word_break(A, dic):
    def helper(A, buf, buf_index, pos, dic, memo):
        if pos == len(A):
            res.append(' '.join(buf[:buf_index].copy()))
            return

        #if not memo.get(pos, True):
        #    return False

        for i in range(pos, len(A)):
            sub_string = A[pos:i+1]
            if sub_string in dic:
                buf[buf_index] = sub_string
                helper(A, buf, buf_index+1, i+1, dic, memo)
                #if helper(A, buf, buf_index+1, i+1, dic, memo):
                #    return True
                #else:
                #    memo[i+1] = False

        return False

    res = []
    buf = [None] * len(A)
    memo = {}
    helper(A, buf, 0, 0, dic, memo)
    print (memo)
    return res


if __name__ == "__main__":
    print (word_break("iball", ("i", "iall", "ball")))
