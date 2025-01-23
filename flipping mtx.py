class MatrixScore:
    def __init__(self, matrix):
        self.matrix = matrix

    def toggle(self, col):
        for row in range(len(self.matrix)):
            self.matrix[row][col] = 1 - self.matrix[row][col]

    def score(self):
        total = 0
        for row in self.matrix:
            total += int(''.join(map(str, row)), 2)
        return total

    def calculate_maximum_score(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        for col in range(cols):
            ones = sum(self.matrix[row][col] for row in range(rows))
            if ones < rows / 2:  # If toggling the column would increase the number of 1s
                self.toggle(col)

        return self.score()


# Example usage:
matrix = [
    [0, 0, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0]
]

matrix_score = MatrixScore(matrix)
print("Maximum score after toggling:", matrix_score.calculate_maximum_score())
