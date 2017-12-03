def golf(matrix):
    i = len(matrix)
    row = [sum(matrix[j]) for j in range(i)]
    xirtam = [[matrix[x][y] for x in range(i)] for y in range(len(matrix[0]))]
    colomn = [sum(xirtam[j]) for j in range(i)]
    return [row.index(min(i for i in row)), colomn.index(min(i for i in colomn))]


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