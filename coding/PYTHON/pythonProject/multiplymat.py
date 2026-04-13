def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
A = [[1,2,3], [4, 5, 6]]
B = [[7, 8], [9,10], [11,12]]
if len(A[0]) != len(B):
    raise ValueError("Number of columns in A must equal number of rows in B.")
result = matrix_multiply(A, B)
print("Matrix multiplication result:")
for row in result:
    print(row)