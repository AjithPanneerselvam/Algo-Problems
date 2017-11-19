"""
# Qualcomm

Rotate a Square Image Counterclockwise
Time Complexity - O(n*n)
Space Complexity - O(1)

You are given a square 2D image matrix (List of Lists) where each integer represents a pixel. Write a method rotate_square_image_ccw to rotate the image counterclockwise - in-place. This problem can be broken down into simpler sub-problems you've already solved earlier! Rotating an image counterclockwise can be achieved by taking the transpose of the image matrix and then flipping it on its horizontal axis.

Example:
Input image :
1 0
1 0
Modified to :
0 0
1 1
"""

def rotate_square_image_ccw(matrix):
    # Transpose of the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Flipping the rows
    endRow = len(matrix) - 1
    for i in range(len(matrix) / 2):
        for j in range(len(matrix)):
            matrix[i][j], matrix[endRow - i][j] = matrix[endRow - i][j], matrix[i][j]

    return matrix
