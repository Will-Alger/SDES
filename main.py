s_box = {
    1: {
        "0000": "101",
        "0001": "010",
        "0010": "001",
        "0011": "110",
        "0100": "011",
        "0101": "100",
        "0110": "111",
        "0111": "000",
        "1000": "001",
        "1001": "100",
        "1010": "110",
        "1011": "010",
        "1100": "000",
        "1101": "111",
        "1110": "101",
        "1111": "011"
    },
    2: {
        "0000": "100",
        "0001": "000",
        "0010": "110",
        "0011": "101",
        "0100": "111",
        "0101": "001",
        "0110": "011",
        "0111": "010",
        "1000": "101",
        "1001": "011",
        "1010": "000",
        "1011": "111",
        "1100": "110",
        "1101": "010",
        "1110": "001",
        "1111": "100"
    }
}


def xor(a, b):
    a_int = int(a, 2)
    b_int = int(b, 2)
    xor_int = a_int ^ b_int
    xor_binary = bin(xor_int)[2:]
    if len(a) > len(xor_binary):
        xor_binary = "0" * (len(a) - len(xor_binary)) + xor_binary
    elif len(b) > len(xor_binary):
        xor_binary = "0" * (len(b) - len(xor_binary)) + xor_binary
    return xor_binary


def generate_round_keys(key, rounds):
    keys = []
    tmp = key
    for i in range(rounds):
        if i == 0:
            keys.append(tmp[0:8])
        else:
            tmp = (tmp[1:] + tmp[0])
            keys.append(tmp[0:8])
    return keys

def sixToEight(binStr):
    return (binStr[0:2] + binStr[3] + binStr[2:4] + binStr[2] + binStr[4:6])





def sdes(block, keys):
    if len(keys) == 0:
        return block

    ln = block[:len(block) // 2]
    rn = block[len(block) // 2:]

    perm = sixToEight(rn);

    xor1 = xor(perm, keys.pop(0))

    sub = s_box[1][xor1[0:4]] + s_box[2][xor1[4:9]]

    newrn = xor(sub, ln)

    newblock = rn+newrn
    sdes(newblock, keys)









# main method
def __main__():
    round_keys = generate_round_keys("110110111", 4)
    # print(round_keys)
    result = sdes('011101011010', round_keys)
    print(result)


__main__()
