"""
IBM

Time-Complexity - O(log n)
Space-Complexity - O(log n) - Recursive overhead

Given a Binary Search Tree, return the node with the maximum data.

Example:

       4
      / \
     2   8
        / \
       5  10

Output ==> 10 (TreeNode)
"""

class BinaryTree:

    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    def find_max(self,root):
        # Return element should be of type TreeNode
        if root == None:
            return None
        elif root.right_child:
            return self.find_max(root.right_child)
        else:
            return root
