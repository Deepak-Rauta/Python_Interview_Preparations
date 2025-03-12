# class MatrixMultiplication:
#     def __init__(self, A, B):
#         self.A = A
#         self.B = B
#         self.m = len(A)         # Rows in A
#         self.n = len(A[0])      # Columns in A (should match rows of B)
#         self.p = len(B[0])      # Columns in B

#     def multiply(self):
#         # Check if multiplication is possible
#         if len(self.A[0]) != len(self.B):
#             print("Matrix multiplication not possible. Columns of A must match rows of B.")
#             return None

#         # Initialize result matrix with zeros (m x p)
#         result = [[0 for _ in range(self.p)] for _ in range(self.m)]

#         # Matrix multiplication logic
#         for i in range(self.m):            # Loop through rows of A
#             for j in range(self.p):        # Loop through columns of B
#                 for k in range(self.n):    # Loop through columns of A / rows of B
#                     result[i][j] += self.A[i][k] * self.B[k][j]  # Multiply and sum

#         return result

#     def display_result(self, result):
#         if result:
#             print("Resultant Matrix:")
#             for row in result:
#                 print(row)


# # Example matrices
# A = [[1, 2, 3], 
#      [4, 5, 6]]

# B = [[7, 8], 
#      [9, 10], 
#      [11, 12]]

# # Create an instance of the class
# matrix_instance = MatrixMultiplication(A, B)

# # Perform multiplication
# result_matrix = matrix_instance.multiply()

# # Display result
# matrix_instance.display_result(result_matrix)




class Solution:
    def multiply_matrices(self, A, B):
        m = len(A)
        n = len(A[0])
        p = len(B[0])

        result = [[0 for _ in range(p)] for _ in range(m)]

        for i in range(m):
            for j in range(p):
                for k in range(n):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    
A =[[1, 2, 3],
    [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

matrix_instance = Solution()
result = matrix_instance.multiply_matrices(A, B)
print("Result Matrix:")
for row in result:
    print(row)
