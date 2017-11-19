"""
Apple

Find the kth Largest Node in a BST
Time Complexity - O(n)
Space Complexity - O(log n)

Given a
Binary Search Tree
and an integer k, implement a method to find and return it's kth largest node

Example:
       4
      / \
     2   8
        / \
       5  10

K = 2, Output = 8 (TreeNode)

Note: Each node of BinaryTree is represented by a TreeNode. Check out Use Me section to find out it's structure. Your method must return TreeNode
"""

class BinaryTree:

    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
        self.visitedCount = 0

    # Helper Method
    def size(self,root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child))

    def find_kth_largest(self,root,k):
        # Return Element should be of type TreeNode
        if root == None:
            return None

        if root:

            val = self.find_kth_largest(root.right_child, k)
            if val:
                return val


            self.visitedCount += 1
            if self.visitedCount == k:
                return root

            val = self.find_kth_largest(root.left_child, k)
            if val:
                return val
