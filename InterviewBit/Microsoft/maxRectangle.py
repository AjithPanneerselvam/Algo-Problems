"""
https://www.interviewbit.com/problems/max-rectangle-in-binary-matrix/

"""

class Solution:
    def longestOnes(self, arr):
        maxOnes = 0
        currOnes = 0
        maxUp = 0
        maxDown = 0
        up = 0
        down = 0
        inSearch = False 

        for i in range(len(arr)):
            if(arr[i] == 1 and inSearch):
                down += 1
                currOnes +=1 
            elif(arr[i] == 1 and not(inSearch)):
                inSearch = True 
                up = i 
                down = i
                currOnes = 1 
            else:
                if(inSearch == True):
                    if(currOnes > maxOnes):
                        maxOnes = currOnes
                        maxUp = up 
                        maxDown = down
                        inSearch = False 
        
        if(inSearch):
            if(currOnes > maxOnes):
                        maxOnes = currOnes
                        maxUp = up 
                        maxDown = down
                        inSearch = False 
        
        return maxUp, maxDown


    def add(self, temp, arr, col):
        for i in range(len(temp)):
            if(arr[i][col] == 0):
                temp[i] = 0
        return temp
        
        
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        left = right = 0
        maxArea = 0
        
        for l in range(len(A[0])):
            temp = [1] * len(A) 
            for r in range(l, len(A[0])):
                temp = self.add(temp, A, r)
                
                up, down = self.longestOnes(temp)
                # print("temp l, r, up, down", temp, l, r, up, down)
                if((r - l + 1) * (down - up + 1) > maxArea):
                    maxArea = (r - l + 1) * (down - up + 1)
                    print(l, r, up, down, maxArea)
        
        return maxArea

obj = Solution()
arr = [
  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
  [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
  [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
]
print(obj.maximalRectangle(arr))