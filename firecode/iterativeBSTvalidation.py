"""
asana
"""

# Collections module has already been imported.
class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node


    def validate_BST_Itr(self,root):
        # Return type should be Boolean
        class TreeBoundaryNode:
            def __init__(self, tree_node = None, left_boundary = None, right_boundary = None):
                self.tree_node = tree_node
                self.left_boundary = left_boundary
                self.right_boundary = right_boundary

        if root == None or (root.left_child == None and root.right_child == None):
            return True

        queue = deque()
        queue.append(TreeBoundaryNode(root,-sys.maxint- 1,sys.maxint))
        while queue:
            tree_binary_node = queue.popleft()
            tree_node = tree_binary_node.tree_node
            if (tree_node.data <= tree_binary_node.left_boundary) or (tree_node.data >= tree_binary_node.right_boundary):
                return False

            if tree_node.left_child != None:
                queue.append(TreeBoundaryNode(tree_node.left_child,tree_binary_node.left_boundary,tree_node.data))

            if tree_node.right_child != None:
                queue.append(TreeBoundaryNode(tree_node.right_child,tree_node.data, tree_binary_node.right_boundary))

        return True
