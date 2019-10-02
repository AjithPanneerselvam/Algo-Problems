/*
 * https://leetcode.com/problems/roman-to-integer
 * Time Complexity - O(n), n is the length of roman string 
 * Space Complexity - O(1), map is of constant size
 */

#include<bits/stdc++.h> 
using namespace std; 


class Solution {
public:
    map<char, int> getRomanToInt() {
        map<char, int> romanToInt = {
            make_pair('I', 1),
            make_pair('V', 5),
            make_pair('X', 10),
            make_pair('L', 50),
            make_pair('C', 100),
            make_pair('D', 500),
            make_pair('M', 1000)
        };  
        
        return romanToInt;
    }
    
    int romanToInt(string s) {
        map<char, int> romanToInt = getRomanToInt(); 
        int integer = 0; 
        
        for (int i = 0; i < s.size(); i++) {
            if (i + 1 < s.size() && romanToInt[s[i]] < romanToInt[s[i+1]]) {
                integer = integer + (romanToInt[s[i+1]] - romanToInt[s[i]]);
                i += 1;
            } else {
                integer += romanToInt[s[i]];
            }
        }
        
        return integer; 
    }
};
