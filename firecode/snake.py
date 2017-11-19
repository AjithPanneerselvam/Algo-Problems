"""
Microsoft

Let's have some fun with 2D Matrices! Write a method find_spiral to traverse a 2D matrix (List of Lists) of ints in a clockwise spiral order and append the elements to an output List of Integers.

Example:
Input Matrix :
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]

Output List:[1, 2, 3, 6, 9, 8, 7, 4, 5]
"""

def right(matrix, outputList, row, startColumn, endColumn):
    for column in range(startColumn, endColumn):
        outputList.append(matrix[row][column])

def down(matrix, outputList, startRow, endRow, column):
    for row in range(startRow, endRow):
        outputList.append(matrix[row][column])

def left(matrix, outputList, row, startColumn, endColumn):
    for column in range(startColumn, endColumn, -1):
        outputList.append(matrix[row][column])

def up(matrix, outputList, startRow, endRow, column):
    for row in range(startRow, endRow, -1):
        outputList.append(matrix[row][column])


def find_spiral(matrix):
    outputList = []
    n = len(matrix)

    for i in range(int(n/2)):
            right(matrix, outputList, i, i, len(matrix[i]) - i)
            down(matrix, outputList, i + 1, n - i, len(matrix[i]) - i - 1)
            left(matrix, outputList, n - i - 1, len(matrix[i]) - i - 2, i - 1)
            up(matrix, outputList, n - i - 2, i, i)

    if n % 2:
        row = int(n/2)
        for column in range(int(n/2), len(matrix[row]) - int(n/2)):
            outputList.append(matrix[row][column])

    return outputList

# print (find_spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
