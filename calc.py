def convert_to_dec(str_number, radix):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if radix <= 0:
        return -1
    if radix > 36:
        return -1
    for i in alphabet:
        for j in str_number:
            if i == j:
                if radix >= alphabet.index(i) + 1:
                    continue
                else:
                    return -1
    k = 0
    sum = 0
    for i in str_number:
        for j in alphabet:
            if j == str_number[len(str_number) - 1 - k]:
                sum += alphabet.index(j) * radix ** k
                k += 1
                break
    return sum


def convert_from_dec(str_number, radix):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if radix <= 0:
        return -1
    if radix > 36:
        return -1
    for i in alphabet:
        for j in str_number:
            if i == j:
                if j < alphabet[10]:
                    continue
                else:
                    return -1
    while


if __name__ == '__main__':

    print(convert_from_dec("199", 2))

