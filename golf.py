def golf(matrix):
    sum_row, sum_col = 0, 0
    for a in matrix[0]:
        sum_row += a
    i = 0
    for a in range(len(matrix)):
        sum_col += matrix[i][0]
        i += 1
    i, n, sum = 0, 0, 0
    for a in matrix:
        for b in matrix[i]:
            sum += b
        if sum_row > sum:
            sum_row = sum
            n = i
        sum = 0
        i += 1
    i, j, k, sum = 0, 0, 0, 0
    for a in range(len(matrix)):
        for b in matrix:
            sum += matrix[i][j]
            i += 1
        if sum_col > sum:
            sum_col = sum
            k = j
        sum = 0
        j += 1
        i = 0
    res = [n,k]
    return res


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert golf([[7, 2, 7, 2, 8],
                 [2, 9, 4, 1, 7],
                 [3, 8, 6, 2, 4],
                 [2, 5, 2, 9, 1],
                 [6, 6, 5, 4, 5]]) == [3, 3], "3,3"
    assert golf([[7, 2, 4, 2, 8],
                 [2, 8, 1, 1, 7],
                 [3, 8, 6, 2, 4],
                 [2, 5, 2, 9, 1],
                 [6, 6, 5, 4, 5]]) == [1, 2], "1,2"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")