/*
 * https://leetcode.com/problems/longest-common-prefix/
 * Time Complexity - O(m * n), where is the no. of strings given and n is the smallest length of the string among the given strings 
 * Space Complexity - O(1)
 */

#include<bits/stdc++.h> 
using namespace std; 

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string result;
        if (strs.size() == 0) {
            return result;
        }
        
        int smallestStringLen = INT_MAX;
        for (int i = 0; i < strs.size(); i++) {
            int s = strs[i].size();
            smallestStringLen = min(smallestStringLen, s);
        }
        
        for (int i = 0; i < smallestStringLen; i++) {
            char ch = strs[0][i];

            for (int j = 1; j < strs.size(); j++) {
                if(ch != strs[j][i]) {
                    return result; 
                }
            }
            
            result += ch;
        }
        
        return result; 
    }
};
