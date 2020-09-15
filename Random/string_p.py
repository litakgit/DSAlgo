
def solve_valid_paren(A):
    def helper(pos, stack):
        #import pdb; pdb.set_trace()
        if pos == len(A):
            return len(stack) == 0
        if A[pos] == '(':
            if helper(pos+1, stack+['(']):
                return False
        elif A[pos] == ')':
            if not stack or stack.pop() != '(':
                return False
            if helper(pos+1, stack):
                return True
        else:
            for ch in '() ':
                if ch == '(':
                    if helper(pos+1, stack+['(']):
                        return False
                elif ch == ')':
                    if not stack or stack.pop() != '(':
                        return False
                    if helper(pos+1, stack):
                        return True
                    stack.append('(')
                else:
                    if helper(pos+1, stack):
                        return True
        return False

    if helper(0, []):
        print ("Valid pattern")
    else:
        print ("In-Valid pattern")

def solve(A):
    def helper(pos, buf_index, buf):
        if pos == len(A):
            res[0] |= not buf_index
            return res[0]

        if A[pos] == '(':
            buf[buf_index] = '('
            helper(pos+1, buf_index+1, buf)
        elif A[pos] == ')':
            if buf_index == 0 or buf[buf_index - 1] != '(':
                return False
            helper(pos + 1, buf_index-1, buf)
        else:
            for ch in '() ':
                if ch == '(':
                    buf[buf_index] = ch
                    helper(pos+1, buf_index+1, buf)
                elif ch == ')':
                    if buf_index == 0 or buf[buf_index-1] != '(':
                        return False
                    helper(pos+1, buf_index-1, buf)
                else:
                    helper(pos+1, buf_index, buf)

    res = [False]
    buf = ['-'] * len(A)
    helper(0, 0, buf)
    if res[0]:
        print ("Matched")
    else:
        print ("not matched")


def solve1(A):
    def helper(pos, buf_index, buf):
        if pos == len(A):
            return not buf_index

        if A[pos] == '(':
            buf[buf_index] = '('
            if helper(pos+1, buf_index+1, buf):
                return True
        elif A[pos] == ')':
            if buf_index == 0 or buf[buf_index - 1] != '(':
                return False
            if helper(pos + 1, buf_index-1, buf):
                return True
        else:
            for ch in '() ':
                if ch == '(':
                    buf[buf_index] = ch
                    if helper(pos+1, buf_index+1, buf):
                        return True
                elif ch == ')':
                    if buf_index != 0 and buf[buf_index-1] == '(':
                        if helper(pos+1, buf_index-1, buf):
                            return True
                else:
                    if helper(pos+1, buf_index, buf):
                        return True
        return False

    buf = ['-'] * len(A)
    res = helper(0, 0, buf)
    if res:
        print ("Matched")
    else:
        print ("not matched")

# abcbccba
# abca
def get_all_strings_with_unique_chars(A):
    start, end = 0, 0
    res = set()
    #import pdb; pdb.set_trace()
    while start < len(A):
        uniqe_chars = set(A)
        while end < len(A) and uniqe_chars:
            uniqe_chars.discard(A[end])
            end += 1
        if end == len(A) and uniqe_chars:
            break
        res.add(A[start:end])
        for i in range(end, len(A)):
            res.add(A[start:i+1])
        start += 1
        end = start
    return len(res)

if __name__ == "__main__":
    #solve1("(*)(*(*)))") # ( ( ) ( ( ( ) ( ( ( ) ) ) ) ) )
    ##solve1("*)") # ( ( ) ( ( ( ) ( ( ( ) ) ) ) ) )
    #solve_valid_paren("(*)")
    #print (get_all_strings_with_unique_chars("abcbcabca"))
    print (get_all_strings_with_unique_chars("abca"))
