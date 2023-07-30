#!/usr/bin/python3

def validUTF8(data):
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    def is_valid_utf8_character(byte):
        if (byte & 0b10000000) == 0:
            return True

        num_bytes = 0
        for i in range(7, 1, -1):
            if (byte & (1 << i)) == 0:
                break
            num_bytes += 1

        return 1 <= num_bytes <= 4

    i = 0
    while i < len(data):
        byte = data[i]
        if not is_valid_utf8_character(byte):
            return False
        if (byte & 0b10000000) != 0:
            num_continuation_bytes = byte & 0b00111111
            for j in range(1, num_continuation_bytes + 1):
                if i + j >= len(data) or not is_continuation(data[i + j]):
                    return False
            i += num_continuation_bytes

        i += 1

    return True
