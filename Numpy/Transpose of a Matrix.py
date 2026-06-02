def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    c = len(a[0])
    r = len(a)

    matrix = [[0 for _ in range(r)] for _ in range(c)]
    for i in range(c):
        for j in range(r):
            matrix[i][j] = a[j][i]

    return matrix