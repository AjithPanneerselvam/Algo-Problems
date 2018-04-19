"""
https://www.interviewbit.com/problems/distribute-candy/

Time Complexity - O(n)
Space Complexity - O(n)
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        if len(A) == 0:
            return 0
        numChocolates = [1]

        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                numChocolates.append(numChocolates[i-1]+1)
            else:
                numChocolates.append(1)
    
        result = numChocolates[len(A)-1]
        for i in range(len(A)-2,-1,-1):
            if A[i]>A[i+1]:
                numChocolates[i] = max (numChocolates[i], numChocolates[i+1]+1)
            result += numChocolates[i]
    
        return result
     