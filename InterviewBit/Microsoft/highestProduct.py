"""
https://www.interviewbit.com/problems/highest-product/
Time Complexity - O(n log n)
Space Complexity - O(1)
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort()
        
        if(A[len(A) -1] <= 0):
            return A[0] * A[1] * A[2] 
        else:
            return (max(A[0] * A[1] * A[len(A) -1], A[len(A)-1] * A[len(A)-2] * A[len(A)-3] ))
        