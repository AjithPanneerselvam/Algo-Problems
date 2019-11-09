/*
 * https://leetcode.com/problems/search-in-rotated-sorted-array 
 * Time Complexity - O(log n)
 * Space Complexity - O(1) 
 */

#include<bits/stdc++.h> 
using namespace std; 

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int mid = 0; 
        
        while (low <= high) {
            mid = low + int((high - low) / 2);     
            
            if (nums[mid] == target) {
                return mid; 
            } else if (nums[low] == target) {
                return low; 
            } else if (nums[high] == target) {
                return high; 
            }
            
            if (nums[low] <= nums[mid]) {
                if (target > nums[low] && target < nums[mid]) {
                    high = mid - 1; 
                } else {
                    // target may be in right skewed partition 
                    low = mid + 1; 
                }
            } else {
                if (target > nums[mid] && target < nums[high]) {
                    low = mid + 1; 
                } else {
                    // target may be in left skewed partition 
                    high = mid - 1; 
                }
            }
        }
        
        return -1;
    }
};
