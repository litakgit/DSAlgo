
# aabcbaaa
# abcd

def get_smallest_palin_by_appending_only(s):
    l = len(s) - 1
    pos = 0
    while True:
        end = l - pos
        start = 0
        while start < end:
            if s[start] == s[end]:
                start, end = start + 1, end - 1
            else:
                break
        if start >= end:
            break
        pos += 1
    return ''.join(list(reversed(s[-pos:]))) if pos else ''

if __name__ == "__main__":
    s = 'aabcbaaa'
    s = 'asdertyredsa'
    s = 'qaaaaa'
    print (get_smallest_palin_by_appending_only(s))
