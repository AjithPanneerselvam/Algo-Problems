
def maxSumSubarray(A):
    if(len(A) == 1):
        return A[0]
    
    maxSum = -100000
    currentSum = 0

    for i in range(len(A)):
        currentSum += A[i]
        if(currentSum > maxSum):
            maxSum = currentSum
        if(currentSum < 0):
            currentSum = 0
    
    return maxSum


print(maxSumSubarray([1,2,3]))
print(maxSumSubarray([-1, -2, 1, 2, 3, -5]))
print(maxSumSubarray([-2, -1]))
print(maxSumSubarray([-2,1,-3,4,-1,2,1,-5,4]))
