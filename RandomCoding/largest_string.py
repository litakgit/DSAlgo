import string

def get_largest_string(A):
    start = 0
    result = (0, 0)
    char_to_index = {}
    for index, c in enumerate(A):
        if c in char_to_index:
            if (index - 1 - start) > abs(result[0] - result[1]):
                result = (start, index-1)
                start = index
        char_to_index[c] = index

    if (index - start) > abs(result[0] - result[1]):
        result = (start, index)
    return A[result[0] : result[1]+1]



# ( a + b ) - c = q + (z + a)
# (, string.ascii_lower
# ( -> abc
# abc -> +/-, ), =
# +/- -> abc
# ) -> +/-, (, abc, =
def validate_eq(A):
    if not A:
        return True
    no_left_paren = no_right_paren = 0
    equal_seen = False
    for i,c in enumerate(A):
        if no_right_paren > no_left_paren:
            return False
        if i == 0:
            if not (c in string.ascii_lowercase or c == '('):
                return False
        elif A[i-1] == '(':
            # abc
            no_left_paren += 1
            if not (c in string.ascii_lowercase or c == '('):
                return False

        elif A[i-1] in string.ascii_lowercase:
            # +/-, ), =
            if c not in ('+', '-', ')', '='):
                return False
            if c == '=':
                if no_left_paren != no_right_paren:
                    return False

        elif A[i-1] in ('+', '-'):
            # abc
            if not (c in string.ascii_lowercase or c == '('):
                return False

        elif A[i-1] == ')':
            # +/-,  =
            no_right_paren += 1
            if c not in ('+', '-', '=', ')'):
                return False
            if c == '=':
                if no_left_paren != no_right_paren:
                    return False
        elif A[i-1] == '=':
            if equal_seen:
                return False
            equal_seen = True
        else:
            return False

    return equal_seen and no_left_paren==no_right_paren

if __name__ == "__main__":
    print (get_largest_string("abacdf"))
    if validate_eq("((a+(b)))=e)"):
        print ("Correct Eqn")
    else:
        print ("Wrong Eqn")

