"""
https://www.interviewbit.com/problems/add-one-to-number/#


Time Complexity - O(n)
Space Complexity - O(n)
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 1
        result = []
        
        for i in range(len(A) - 1, -1,-1):
            temp = carry + A[i] 
            if(temp >= 10):
                carry = 1
            else:
                carry = 0
                
            result.append(temp % 10)
       
        if(carry):
            result.append(carry)
        
        result = result[::-1]
        
        count = 0
        # Find and remove the MSB 0's
        for i in range(len(result)):
            if(result[i] != 0):
                break 
            count += 1
        
        result = result[count:]
        return result


# sol = Solution()
# print(sol.plusOne([0,0,0,0]))
# print(sol.plusOne([0]))
# print(sol.plusOne([1]))
# print(sol.plusOne([9,9,9]))
