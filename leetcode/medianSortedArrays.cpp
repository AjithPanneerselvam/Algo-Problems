/*
 * https://leetcode.com/problems/median-of-two-sorted-arrays
 */

#include<bits/stdc++.h>
using namespace std; 

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }   
        
        int nums1Len = nums1.size();
        int nums2Len = nums2.size(); 
        int low = 0, high = nums1Len; 
        int partitionNums1, partitionNums2; 
        int maxLeft1, maxLeft2, minRight1, minRight2; 
        
        while (low <= high){
            partitionNums1 = (low + high) / 2; 
            partitionNums2 = ((nums1Len + nums2Len + 1) / 2) - partitionNums1; 

            maxLeft1 = (partitionNums1 == 0)? INT_MIN: nums1[partitionNums1-1];
            maxLeft2 = (partitionNums2 == 0)? INT_MIN: nums2[partitionNums2-1];
            minRight1 = (partitionNums1 == nums1Len)? INT_MAX: nums1[partitionNums1]; 
            minRight2 = (partitionNums2 == nums2Len)? INT_MAX: nums2[partitionNums2]; 
            
            // all the elements in the left partition are lesser than or equal to all the elements in the right
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                if ((nums1Len + nums2Len) % 2) {
                    return max(maxLeft1, maxLeft2);
                } 
                
                return ((double)(max(maxLeft1, maxLeft2) + min(minRight1, minRight2))) / 2; 
            } else if (maxLeft1 > minRight2) {
                high = partitionNums1 - 1; 
            } else {
                low = partitionNums1 + 1; 
            }            
        }
        
        return 0.0;
    }
};
