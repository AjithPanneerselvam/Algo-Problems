/*
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array
 */

#include<bits/stdc++.h> 
using namespace std; 

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        
        int uniqueElements = 1, previousElement = nums[0]; 
        for (int i = 1; i < nums.size(); i++) {
               if (nums[i] == previousElement) {
                   continue; 
               }
                
               previousElement = nums[i];
               nums[uniqueElements] = nums[i]; 
               uniqueElements++;
        }
        
        return uniqueElements;
    }
};
