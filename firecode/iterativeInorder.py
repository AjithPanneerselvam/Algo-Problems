"""
Iterative Inorder Traversal
Time Complexity - O(n)
Space Complexity - O(n)

Given a binary tree, implement a method to perform the inorder traversal iteratively and add the data of each node in a list in the way inorder traversal is printed. Return an empty list in case of an empty tree.

Example:
     1
    / \
   2   3     ==> 4251637
  / \ / \
 4  5 6  7
"""
class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None


    def inorder_iterative(self):
        inorder_list = []
        stack = []
        if self == None:
            return inorder_list

        node = self

        while(len(stack) or node):
            if node:
                stack.append(node)
                node = node.left_child
            else:
                node = stack.pop()
                inorder_list.append(node.data)
                node = node.right_child

        return inorder_list
