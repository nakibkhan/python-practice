import numpy as np

def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])

    rows_B = len(B)
    cols_B = len(B[0])

    result = np.zeros((rows_A, cols_B))

    if cols_A != rows_B:
        raise ValueError("Columns in A should be equal to rows in B")

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

A = [
    [1  , 2 , 3],
    [4  , 5 , 6],
]

B = [
    [7  , 8 ],
    [9  , 10],
    [11 , 12]
]