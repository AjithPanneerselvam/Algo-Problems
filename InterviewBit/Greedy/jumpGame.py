
# InterviewBit Solution 
# Time Complexity - O(n); Space Complexity - O(1)
class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        farthest = 0
        for i in range(len(A)-1):
            farthest = max(farthest, i + A[i])
            if farthest == i:
                return 0
        return 1


# My Solution - 1 
# Time Complexity - O(n); Space Complexity - O(n)
# class Solution:
#     def canJump(self, A):
#         jumpable = [False] * len(A)
#         jumpable[0] = True 

#         for i in range(len(A)-1):
#             if(i + A[i] < len(A)):
#                 jumpable[i + A[i]] = True 
        
#         return jumpable[-1]


# # Common mistake the candidate make (Dynamic Programming Approach)
# # Time Complexity - O(n^2) Space Complexity - O(n)
# class Solution:
#     def canJump(self, A):
#         dynArray = [False] * len(A)
#         dynArray[0] = True 

#         for i in range(len(A)-1):
#             for j in range(i+1, i + A[i] + 1):
#                 if j < len(A):
#                     dynArray[j] = True 
        
#         return dynArray[-1]


obj = Solution()
print(obj.canJump([1,4,2,0,2,0,1]))
