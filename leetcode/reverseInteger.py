"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/description/
Time Complexity - O(1)
Space Complexity - O(1)
"""


class Solution(object):
    def __init__(self):
        self.maxRange = (2 ** 31) - 1


    def reverseInteger(self, x):
        result = 0
        while(x):
            result = (result * 10) + x % 10
            x = int(x / 10)
        return result


    def thirtyTwoBitCheck(self, x):
        print(self.maxRange)
        if(x > self.maxRange):
            return 0
        else:
            return 1


    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            # Make the interger positive
            x = -x
            x = self.reverseInteger(x)

            # Check the number fit it in 32 bit memory
            if(not(self.thirtyTwoBitCheck(x))):
                return 0
            x = -x
        else:
            x = self.reverseInteger(x)
            if(not(self.thirtyTwoBitCheck(x))):
                return 0

        return x
