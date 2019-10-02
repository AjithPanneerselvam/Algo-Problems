/*
 * https://leetcode.com/problems/palindrome-number/
 */ 

#include <bits/stdc++.h> 
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false; 
        }
        
        uint palindrome = 0; 
        int temp = x; 
        while (temp > 0) {
            palindrome = palindrome * 10 + uint(temp) % 10; 
            temp = temp / 10; 
        }
        
        return palindrome == uint(x); 
    }
};
