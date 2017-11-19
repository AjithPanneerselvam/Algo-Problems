"""
Asana

Interative BST Validation
Time Complexity - O(n)
Space Complexity - O(log n)

Given the root node of a Binary Tree, write a method - validate_BST_Itr to iteratively determine if it is a Binary Search Tree.

A BST must satisfy the following conditions :
* The left subtree of a node contains nodes with data < its data.
* The right subtree of a node contains  nodes data > its data.
* A node's left and right subtrees follow the above two conditions.

Examples:


          20
         /   \
       15    30
      /  \
     14  18

    output ==> True

          20
         /   \
       30    15
      /  \
    14   18

   output ==> False
"""


# Collections module has already been imported.
class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node
            self.previousVal = -10000


    def validate_BST_Itr(self,root):
        if root == None:
            return True
        if not(self.validate_BST_Itr(root.left_child)):
            return False
        if root.data < self.previousVal:
            return False
        self.previousVal = root.data
        if not(self.validate_BST_Itr(root.right_child)):
            return False
        return True
