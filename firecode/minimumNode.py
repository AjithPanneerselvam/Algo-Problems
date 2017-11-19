"""
IBM

Time-Complexity - O(log n)
Space-Complexity - O(1)

Return the minimum node in the BST
"""

def minimumNode(root):
    if root == None:
        return None
    if root.left_child == None:
        return root
    else:
        return root.left_child
