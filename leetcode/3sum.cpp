/*
 * https://leetcode.com/problems/3sum 
 * Time Complexity - O(n logn) + O(n ^ 2) 
 * Space Complexity - O(n) for cache 
 */ 

#include<bits/stdc++.h>
using namespace std; 

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {     
        if (nums.size() < 3) {
            return vector<vector<int>>{};
        }
        
        vector<vector<int>> result; 
        set<vector<int>> cache;
        
        int a, b, c; 
        a = b = c = 0;
        
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size() - 2; i++) {  
            a = nums[i];
            int j = i + 1;
            int k = nums.size() - 1; 
            
            while (j < k) {
                b = nums[j];
                c = nums[k];
                
                int sum = a + b + c; 
                if (sum == 0) {
                    result.push_back(vector<int>{a, b, c});    
                    j++; 
                    k--;
                } else if (sum < 0) {
                    j++;
                } else {
                    k--; 
                }
            }
            
        }
        
        for (auto itr = result.begin(); itr != result.end(); itr++) {
            cache.insert(*itr); 
        }
        
        result = vector<vector<int>>{cache.begin(), cache.end()};      
        return result;
    }
};
