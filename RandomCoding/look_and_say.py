
# 1, 11, 21, 1211, 111221, 312211, 13112221

# You need to return the nth no in the seq.

def get_nth_seq(n):
    def get_next_seq(prev):
        count = 1
        res = []
        for i in range(1, len(prev)+1):
            if i < len(prev) and prev[i] == prev[i-1]:
                count += 1
            else:
                res.append(str(count)+prev[i-1])
                count = 1
        return ''.join(res)

    k = "1"
    for _ in range(n):
        k = get_next_seq(k)

    return k

if __name__ == "__main__":
    n = get_nth_seq(5)
    print (n)
