def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	c = len(matrix[0])
	r = len(matrix)
	for i in range(c):
		for j in range(r):
			matrix[i][j] = matrix[i][j] * scalar

	return matrix