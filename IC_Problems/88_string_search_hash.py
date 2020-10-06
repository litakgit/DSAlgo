
def get_string_match(s, pattern):
    z = 26
    h_pattern, rolling_hash = 0, 0

    for ch in pattern:
        h_pattern = h_pattern * z + ord(ch)

    for i in range(len(pattern)):
        rolling_hash = rolling_hash * z + ord(s[i])

    if (h_pattern == rolling_hash and
        pattern == s[0:len(pattern)]):
            return 0

    base = z ** max((len(pattern)-1, 0))

    for i in range(len(pattern), len(s)):
        # Calculate the rolling hash. Calculate in pen and paper.
        rolling_hash -= base * ord(s[i-len(pattern)])
        rolling_hash = rolling_hash * z
        rolling_hash += ord(s[i])

        if (h_pattern == rolling_hash and
            pattern == s[i-(len(pattern)-1) : i+1]):
                return i-len(pattern)+1

    return -1

if __name__ == "__main__":
    print (get_string_match("abcmnxyzwert", "mnx"))
