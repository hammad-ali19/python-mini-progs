# Problem 16: Matrix Multiplication

# Write a Python function that takes two matrices (2D lists) as input and returns their 
# product. Ensure that the number of columns in the first matrix is equal to the number of 
# rows in the second matrix.

def matrix_multiply (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return ("Multiplication Impossible")
    
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(rows_B):
                C[i][j] += A[i][k] * B[k][j]
    return C


C = matrix_multiply([[1,2], [3,4]], [[5,6], [7,8]])
print(C)
