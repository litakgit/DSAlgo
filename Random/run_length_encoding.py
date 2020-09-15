
# aaabccdeeef -> 3a1b2c1d3e1f

# aab

def encode(to_be_encoded):
    count = 1
    res = []
    for i in range(1, len(to_be_encoded)+1):
        if i < len(to_be_encoded) and to_be_encoded[i] == to_be_encoded[i-1]:
            count += 1
        else:
            res.append(str(count)+to_be_encoded[i-1])
            count = 1
    return ''.join(res)

def decode(to_be_decoded):
    #import pdb; pdb.set_trace()
    count = 0
    res = []
    for ch in to_be_decoded:
        if ch.isdigit():
            count = count * 10 + int(ch)
        else:
            res.append(ch * count)
            count = 0
    return ''.join(res)

if __name__ == "__main__":
    to_be_encoded = "aaaabccffffd"
    encoded = encode(to_be_encoded)
    print (to_be_encoded, encoded)
    decoded = decode(encoded)
    print (decoded, "<-",  encoded)
