"""
https://www.interviewbit.com/problems/majority-element/

Time Complexity - O(n)
Space Complexity - O(1)
"""

class Solution:
    def mooreVotingAlgorithm(self, arr):
        count = 1
        maxIndex =  0
    
        for i in range(1, len(arr)):
            if(arr[maxIndex] == arr[i]):
                count += 1
            else:
                count -= 1
            
            if(count == 0):
                maxIndex = i 
                count = 1
        
        return arr[maxIndex]


    def checkMajorityElement(self, arr, val):
        count = 0
        for i in range(len(arr)):
            if(arr[i] == val):
                count += 1
        
        if(count > len(arr)//2):
            return 1
        else:
            return 0
    
    
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        majElement = self.mooreVotingAlgorithm(A)
        if(self.checkMajorityElement(A, majElement)):
            return majElement
        else:
            return -1