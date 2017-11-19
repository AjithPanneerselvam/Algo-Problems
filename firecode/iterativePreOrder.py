"""
Iterative Preorder Traversal

Given a binary tree, write a function to iteratively traverse the tree in the preorder manner. Mark a node as visited by adding its data to a list.
Return an empty list in the case of an empty tree.

Example:
     1
    / \
   2   3     ==> 1245367
  / \ / \
 4  5 6  7 
"""

class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder_iterative(self):
        pre_ordered_List = []
        stack = []

        if self == None:
            return None

        node = self
        while(len(stack) or node):
            if node:
                stack.append(node)
                pre_ordered_List.append(node.data)
                node = node.left_child
            else:
                node = stack.pop()
                node = node.right_child

        return pre_ordered_List
