def matrix_rotation(matrix):
    # First step is transpose the matrix
    transpose_matrix = list(zip(*matrix))
    # Second step is reverse each row in the transposed matrix
    rotated_matrix = [list(row)[::-1] for row in transpose_matrix]
    return rotated_matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotated = matrix_rotation(matrix)
for row in rotated:
    print(row)