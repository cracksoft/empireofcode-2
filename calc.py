def convert(str_number, radix):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if radix == 0:
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


if __name__ == '__main__':

    print(convert("100000", 2))

