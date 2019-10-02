/*
https://leetcode.com/problems/container-with-most-water 
* Time Complexity - O(n)
* Space Complexity - O(1)
*/

#include<bits/stdc++.h> 
using namespace std; 

class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0, j = height.size() -1, maxContainer = 0;
        
        while (i < j) {
            maxContainer = max(maxContainer, (j - i) * min(height[i], height[j])); 
            
            if (height[i] <= height[j]) {
                i++; 
            } else{
                j--;
            }
        }
        
        return maxContainer;
    }
};
