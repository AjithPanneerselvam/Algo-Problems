"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description

Accepted
Time Complexity - O(n)
Space Complexity - O(n)
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestSubstring = 1
        currentCount = maxCount = 0
        dictionary = {}
        startIndex = 0

        for i in range(len(s)):

            if s[i] not in dictionary:
                dictionary[s[i]] = i
                currentCount += 1

            elif s[i] in dictionary:
                if dictionary[s[i]] >= startIndex:
                    startIndex = dictionary[s[i]] + 1
                    currentCount = i - dictionary[s[i]]
                else:
                    currentCount += 1

            if maxCount < currentCount:
                    maxCount = currentCount

            dictionary[s[i]] = i

        return maxCount
