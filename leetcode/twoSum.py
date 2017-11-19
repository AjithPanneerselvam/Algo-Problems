"""
https://leetcode.com/problems/two-sum/#/description

Accepted
Time Complexity - O(n)
Space Complexity - O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dictionary = dict()
        result = []

        for i in range(len(nums)):
            diff = target - nums[i]
            # Lookup operation in the dictionary - O(1)
            if diff in dictionary:
                result.append(dictionary[diff])
                result.append(i)
                return result
            dictionary[nums[i]] = i

        return []
