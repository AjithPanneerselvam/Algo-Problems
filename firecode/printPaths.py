"""
# Microsoft
Time-Complexity - O(b^d), where b is the branching factor and d is the depth; b = 2 and d = m + n in this case
Space-Complexity - O(bd)

Print Paths
You're given a 2D board which contains an m x n matrix (2D list of characters).
Write a method - print_paths that prints all possible paths from the top left cell to the bottom right cell.
Your method should return a list of strings, where each string represents a path with characters appended in the order of movement.
You're only allowed to move down and right on the board. The order of string insertion in the list does not matter.
Example:
Input Board :
[
    [A, X],
    [D, E]
]
Output: ["ADE", "AXE"]
"""

def addPath(board, paths, currentString, row, column, rowLen, colLen):
    if row == rowLen:
        return
    if column == colLen:
        return

    currentString += board[row][column]

    if row + 1 == rowLen and column + 1 == colLen:
        paths.append(currentString)

    addPath(board, paths, currentString, row, column + 1, rowLen, colLen)
    addPath(board, paths, currentString, row + 1, column, rowLen, colLen)

def print_paths(board):
    paths = list()
    if len(board) == 0:
        return []
    if len(board) == 1 and len(board[0]) == 1:
        paths.append(board[0][0])
        return paths

    addPath(board, paths, "", 0, 0, len(board), len(board[0]))
    return paths
