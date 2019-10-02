/*
 * https://leetcode.com/problems/zigzag-conversion
 *
 * Time Complexity - O(m); where is the length of the string 
 * Space Complexity - O(1) 
 * */

#include<bits/stdc++.h> 
using namespace std; 


class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s; 
        }
        
        string result; 
        int index = 0, temp;
        int n = numRows; 
        
        for (int i = 0; i < numRows; i++) {
            if (i == 0 || i == numRows - 1) {
                index = i;
                while(index < s.size()) {
                    result += s[index];
                    index += (n - 1) + (n - 2) + 1; 
                }
            } else {
                index = i;
                while (index < s.size()) {
                    result += s[index];
                    
                    temp = index + 2 * (n - i -1);  
                    if (temp < s.size()) {
                        result += s[temp]; 
                    } else {
                        index = temp;
                        continue; 
                    }
                    
                    index += (n - i - 1) + (n - 2) + (i + 1);
                }
            }
        }
        
        return result; 
    }
};
