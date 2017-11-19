"""
# Microsoft

Number of Full Nodes in a Binary Tree
Write a function to iteratively determine the total number of "full nodes" in a binary tree.
A full node contains left and right child nodes.
If there are no full nodes, return 0.

Example:

       1
      / \
     2   3
    / \ / \
   4  5 6  7
  / \
 8   9

Full nodes count ==> 4
"""

class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    # Required collection modules have already been imported.
    def number_of_full_nodes(self,root):
        if root == None:
            return 0
        elif root.left_child != None and root.right_child != None:
            return 1 + self.number_of_full_nodes(root.left_child) + self.number_of_full_nodes(root.right_child)
        elif root.left_child:
            return self.number_of_full_nodes(root.left_child)
        elif root.right_child:
            return self.number_of_full_nodes(root.right_child)
        else:
            return 0
