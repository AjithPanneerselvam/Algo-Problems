/*
 * https://leetcode.com/problems/longest-valid-parentheses/ 
 * Time Complexity - O(n) 
 * Space Complexity - O(n) for stack
 */

# include <bits/stdc++.h> 
using namespace std; 

class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st; 
        
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                st.push(i); 
            } else {
                if (st.empty()) {
                    st.push(i); 
                } else if (s[st.top()] == ')'){
                    // match not found for `)`
                    st.push(i); 
                } else {
                    // match found for `)` 
                    st.pop(); 
                }
            }
        }
        
        if (st.empty()) {
            // The given string is completely valid 
            return s.length(); 
        }
        
        int prevTop = s.length();
        int currentTop = 0; 
        int maxValidLength = 0; 
        
        while (!st.empty()) {
            currentTop = st.top();
            st.pop(); 

            // consecutive mistmatches 
            if (prevTop - 1 == currentTop) {
                prevTop = currentTop; 
                continue;
            }
            
            maxValidLength = max(maxValidLength, prevTop - currentTop - 1);
            prevTop = currentTop; 
        }
        
        if (prevTop == s.length()) {
            return prevTop - 1; 
        } 
        
        return max(prevTop, maxValidLength); 
    }
};
