"""
Qualcomm

Find the Transpose of a Square Matrix
You are given a square 2D image matrix (List of Lists) where each integer represents a pixel. Write a method transpose_matrix to transform the matrix into its Transpose - in-place. The transpose of a matrix is a matrix which is formed by turning all the rows of the source matrix into columns and vice-versa.

Example:
Input image :
1 0
1 0

Modified to:
1 1
0 0
"""

def transpose_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(row,len(matrix[row])):
            matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
    print(matrix)
