import numpy as np

from algorithms.matrices.matrix_multiply import matrix_multiply


def matrix_transposed(A):
    rows_A = len(A)
    cols_A = len(A[0])

    result = np.zeros((cols_A, rows_A))

    for i in range(rows_A):
        for j in range(cols_A):
            result[j][i] = A[i][j]

    return result

A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

print(matrix_transposed(matrix_multiply(matrix_transposed(A), A)))
print(matrix_multiply(matrix_transposed(A), A))