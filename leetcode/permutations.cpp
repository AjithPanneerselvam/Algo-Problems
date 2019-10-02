// https://leetcode.com/problems/permutations

#include <bits/stdc++.h> 
using namespace std; 

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result; 
        printPermutation(nums, result, 0, nums.size());
        return result;
    }
    
    void swap(vector<int>& nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    void printPermutation(vector<int>& nums, vector<vector<int>>& result, int i, int len) {
        if (i == len) {
            result.push_back(nums);
            return;
        }
        
        for (int j = i; j < len; j++) {
            swap(nums, i, j);
            printPermutation(nums, result, i+1, len);
            swap(nums, i,j); 
        }
    }
};
