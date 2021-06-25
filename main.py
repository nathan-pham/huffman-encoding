table = {
    "00": "A",
    "11": "E",
    "010": "T",
    "0110": "C",
    "0111": "U",
    "1000": "S",
    "1011": "R",
    "10010": "O",
    "10011": "I",
    "101000": "N",
    "101001": "M",
    "101010": "H",
    "101011": "Y"
}

def decode_binary(string):
    decoded_string = ""
    cache = ""

    for char in string:
        cache += char
        match = table.get(cache)

        if match is not None:
            decoded_string += match
            cache = ""

    return decoded_string

print(decode_binary("10101010010101000111000010101011"))
print(decode_binary("10101010010101000100101011"))