"""
Linkedin

Maximum Sum Path
Time Complexity - O(n)
Space Complexity - O(log n)

Given a binary tree consisting of nodes with positive integer values, write a method - max_sum_path that returns the maximum sum of data values obtained by traversing nodes along a path between any 2 nodes of the tree. The path must originate and terminate at 2 different nodes of the tree, and the maximum sum is obtained by summing all the data values of the nodes traversed along this path.

Example:

     1
    / \
   2   3     => 18
  / \ / \
 4  5 6  7

Path: 5 -> 2 -> 1 -> 3 -> 7
Max Sum = 5+2+1+3+7 = 18
"""


class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node
            self.maxSum = 0

    # All the necessary collection moduled have been already imported.
    def max_sum_path(self,root, isRoot = True):
        if root == None:
            return 0

        leftTreeVal = self.max_sum_path(root.left_child, False)
        rightTreeVal = self.max_sum_path(root.right_child, False)

        if isRoot:
            return leftTreeVal + root.data + rightTreeVal

        if leftTreeVal >= rightTreeVal:
            maxVal =  leftTreeVal + root.data
        else:
            maxVal = rightTreeVal + root.data


        return maxVal
