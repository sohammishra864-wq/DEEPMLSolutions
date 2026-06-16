def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]]:
    a_c = len(a[0])
    a_r = len(a)
    b_c = len(b[0])
    b_r = len(b)
    c = [[0 for _ in range(b_c)] for _ in range(a_r)]
    if a_c != b_r:
        return -1

    for i in range(a_r):
        for j in range(b_c):
            for k in range(a_c):
                c[i][j] += a[i][k] * b[k][j]
    return c

