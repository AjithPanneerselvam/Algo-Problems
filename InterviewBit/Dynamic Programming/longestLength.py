"""
https://www.interviewbit.com/problems/largest-distance-between-nodes-of-a-tree/

Asked In:
Facebook
Google
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        dynArray = [0] * len(A)
        firstLargest = secondLargest = 0
        
        for i in range(1, len(A)):
            depth = 0
            j = i
            while(A[j] != -1):
                j = A[j]
                depth += 1
                if(dynArray[j] != 0):
                    break
            dynArray[i] = depth + dynArray[j]
            
            if(dynArray[i] > firstLargest):
                secondLargest = firstLargest
                firstLargest = dynArray[i]

        return firstLargest + secondLargest


# arr = [ -1, 0, 1, 1, 2, 0, 5, 0, 3, 0, 0, 2, 3, 1, 12, 14, 0, 5, 9, 6, 16, 0, 13, 4, 17, 2, 1, 22, 14, 20, 10, 17, 0, 32, 15, 34, 10, 19, 3, 22, 29, 2, 36, 16, 15, 37, 38, 27, 31, 12, 24, 29, 17, 29, 32, 45, 40, 15, 35, 13, 25, 57, 20, 4, 44, 41, 52, 9, 53, 57, 18, 5, 44, 29, 30, 9, 29, 30, 8, 57, 8, 59, 59, 64, 37, 6, 54, 32, 40, 26, 15, 87, 49, 90, 6, 81, 73, 10, 8, 16 ]
# sol = Solution()
# sol.solve(arr)