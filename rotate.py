def rotate_list(elements, rotates):
    for i in range(rotates):
        a = -1
        y = 0
        x = elements[a]
        for n in range(len(elements) - 1):
            if a % 2 != 0:
                y = elements[a - 1]
                elements[a - 1] = x
            else:
                x = elements[a - 1]
                elements[a - 1] = y
            a -= 1
        elements[-1] = y
    print(elements)
    return elements

if __name__ == '__main__':
    assert rotate_list([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2], "First"
    assert rotate_list([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6, 1, 2, 3], "Second"
    assert rotate_list([1, 2, 3, 4, 5, 6], 0) == [1, 2, 3, 4, 5, 6], "Third"

    print("All set? Click \"Check\" to review your code and earn rewards!")