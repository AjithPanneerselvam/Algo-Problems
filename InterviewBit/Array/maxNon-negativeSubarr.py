class Solution:
    def helper(self, currentSum, maxSum, maxStartIndex, runningIndex, maxLength, i):
        if(currentSum > maxSum):
                maxSum, maxStartIndex, runningIndex, maxLength = currentSum, runningIndex, i + 1, i - runningIndex 
                
        elif(currentSum == maxSum):
            if(i - runningIndex > maxLength or runningIndex < maxStartIndex):
                maxSum, maxStartIndex, runningIndex, maxLength = maxSum, runningIndex, i + 1, i - runningIndex
                
        return (maxSum, maxStartIndex, i + 1, maxLength, 0)
    

    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        maxLength = 0
        maxSum = -1000000
        maxStartIndex = 0
        currentSum = 0
        runningIndex = 0
        index = 0
        firstPositive = False


        for i in range(len(A)):
            if(A[i] < 0 and not(firstPositive)):
                runningIndex = i + 1
                maxStartIndex = i + 1 
            elif(A[i] < 0):
                maxSum, maxStartIndex, runningIndex, maxLength, currentSum = self.helper(currentSum, maxSum, maxStartIndex, runningIndex, maxLength, i)
            else:
                currentSum += A[i] 
                firstPositive = True  
            index += 1

        if(runningIndex == 0):
            return A
        
        maxSum, maxStartIndex, runningIndex, maxLength, currentSum = self.helper(currentSum, maxSum, maxStartIndex, runningIndex, maxLength, index)
        
        return A[maxStartIndex: maxStartIndex + maxLength]
            

sol = Solution()
print(sol.maxset([1,2,5, -7, 2, 3]))
print(sol.maxset([1,2,5]))
print(sol.maxset([1]))
print(sol.maxset([1,2,5, -7, 1, 2, 5]))
print(sol.maxset([1,2,5, -7, -8, 9, 2, 5]))
print(sol.maxset([-1,-2,-1]))
print(sol.maxset([1,2,5,9 -7, -8, 9, -2, 5, 12]))
print(sol.maxset([]))
print(sol.maxset([ 0, 0, -1, 0 ]))
print(sol.maxset([ -1, -2, 0, 0, 0, 0 , -2, -1, 5, 4, -5, -6, 4, 5]))
print(sol.maxset([2, 0,0,0,0, -1]))