"""
687. Longest Univalue Path
https://leetcode.com/problems/longest-univalue-path/description/

Time Complexity - O(n)
Space Complexity - O(1)
"""


class Solution(object):
    def findLongestPath(self, node):
        if node == None:
            return 0

        leftHolder = self.findLongestPath(node.left)
        rightHolder = self.findLongestPath(node.right)
        leftLen = rightLen = 0

        if node.left and node.val == node.left.val:
            leftLen = leftHolder + 1
        if node.right and node.val == node.right.val:
            rightLen = rightHolder + 1

        self.maxVal = max(self.maxVal, leftLen + rightLen)

        return (max(leftLen, rightLen))

    def longestUnivaluePath(self, root):
        self.maxVal = 0
        self.longestUniVal = self.findLongestPath(root)
        return self.maxVal
