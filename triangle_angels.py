def angles(a, b, c):
    gipo = 0
    if a > c:
        gipo = a
    elif b > c:
        gipo = b
    else:
        gipo = c
    if a > b:
        gipo = a
    if gipo >= a + b + c - gipo:
        return [0, 0, 0]



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
