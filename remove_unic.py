def non_unique(data):
    a = 0
    b = 0
    mark = []
    non_uniq = []
    for n in data:
        if type(n) == str:
            if (n.upper() in non_uniq):
                a += 1
                b = 0
                continue
        elif (n in non_uniq):
            a += 1
            b = 0
            continue
        for k in data:
            if a == b:
                if len(data) == b + 1:
                    mark.append(n)
                    break
                b += 1
                continue
            if len(data) == b + 1:
                if type(n) == str:
                    if type(k) == str:
                        x = n.upper()
                        y = k.upper()
                        if x == y:
                            break
                if n == k:
                    break
                mark.append(n)
                break
            if type(n) == str:
                if type(k) == str:
                    x = n.upper()
                    y = k.upper()
                    if x != y:
                        b += 1
                        continue
                    else:
                        non_uniq.append(n)
                        break
            if n != k:
                b += 1
                continue
            non_uniq.append(n)
            break
        a += 1
        b = 0
    for i in mark:
        data.remove(i)
    print(data)
    return data


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert isinstance(non_unique([1]), list), "The result must be a list"
    assert non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert non_unique([1, 2, 3, 4, 5]) == [], "2nd example"
    assert non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"

    # Rank 2
    assert non_unique(['P', 7, 'j', 'A', 'P', 'N', 'Z', 'i',
                       'A', 'X', 'j', 'L', 'y', 's', 'K', 'g',
                       'p', 'r', 7, 'b']) == ['P', 7, 'j', 'A', 'P', 'A', 'j', 'p', 7], "Letters"

    print("All done? Earn rewards by using the 'Check' button!")