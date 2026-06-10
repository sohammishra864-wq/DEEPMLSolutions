def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    eigenvalues = []
    d = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    t = matrix[0][0] + matrix[1][1]
    root = t * t - 4 * d

    if root < 0:
        return eigenvalues
    else:
        root1 = (t + root ** 0.5) / 2
        root2 = (t - root ** 0.5) / 2
        eigenvalues.append(root1)
        eigenvalues.append(root2)
        eigenvalues.sort(reverse=True)
    return eigenvalues