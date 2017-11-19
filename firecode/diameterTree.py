"""
# Google

Find the Diameter of a Binary Tree
Time Complexity - O(n)
Space Complexity - O(1)

Given a Binary Tree, write a method to return its diameter. The diameter of a Binary Tree is defined as the "Number of nodes on the longest path between two leaf nodes".

Example:
       20
      /   \
    15     30
   /  \      \  output => 7
  14  18     35
     /  \    /
  17   19  32

Note:
Each node of BinaryTree is represented by a TreeNode. Check out Use Me section to find out it's structure.
Return type of diameter method should be an integer  and it should execute in O(n) time complexity.
"""

class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node


    def diameter(self,root, isRoot = True):
        if root == None and isRoot:
            return 0

        if root == None:
            return 0,0

        ldiameter, leftSize = self.diameter(root.left_child, False)
        rdiameter, rightSize = self.diameter(root.right_child, False)

        currentSize = leftSize + 1 + rightSize
        maxDiameter = max(ldiameter, rdiameter, currentSize)


        if isRoot == True:
             return maxDiameter

        return (maxDiameter, max(leftSize, rightSize) + 1)
