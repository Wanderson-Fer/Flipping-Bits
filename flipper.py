def convert_to_bits(n):
    converted_n = ''

    for e in range(31, -1, -1):
        if n - 2 ** e >= 0:
            converted_n += '1'
            n -= 2**e
        else:
            converted_n += '0'

    return converted_n


def convert_from_bits(b):
    converted_b = 0
    for e in range(1, 33):
        if b[-e] == '1':
            converted_b += 2 ** (e - 1)

    return converted_b


def flipping_bits(n):
    # Write your code here
    n_in_bits = convert_to_bits(n)

    n_bits_flipped = ''
    for bit in n_in_bits:
        if bit == '0':
            n_bits_flipped += '1'
        else:
            n_bits_flipped += '0'

    n_int_flipped = convert_from_bits(n_bits_flipped)

    return n_int_flipped


if __name__ == '__main__':
    print(f'15 in bits (32) is: {convert_to_bits(15)}')
    print(f'15 flipped like 32bits is: {flipping_bits(15)}')
