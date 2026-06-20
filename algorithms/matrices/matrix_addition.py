import numpy as np

def matrix_addition(A, B):
    result = []
    rows = len(A)
    cols = len(A[0])

    if rows != len(B) or cols != len(B[0]):
        raise ValueError('Matrices must have same dimensions')

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])

        result.append(row)

    return result

A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

B = [
        [7  , 8 , 9 ],
        [10 , 11, 12]
]

print(matrix_addition(A, B))