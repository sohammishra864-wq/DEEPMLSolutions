def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    if len(a[0]) != len(b):
        return -1
    result = []
    for row in a:
        dot = 0
        for j in range(len(b)):
            dot = dot + row[j] * b[j]
        result.append(dot)
    return result
