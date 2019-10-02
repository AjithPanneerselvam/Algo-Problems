/*
 * https://leetcode.com/problems/regular-expression-matching 
 */

#include<bits/stdc++.h> 
using namespace std; 

class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector <bool>> dp(s.size()+1, vector<bool> (p.size() +1, false));
        
        dp[0][0] = true;    // empty pattern and empty string equals true 
        
        // init for empty string and the pattern 
        for (int j = 1; j < dp[0].size(); j++) {
            if (p[j-1] == '*') {
                if ((j > 1 && dp[0][j-2])) {
                    dp[0][j] = true;
                }
            }
        }
        
        for (int i = 1; i < dp.size(); i++) {
            for (int j = 1; j < dp[i].size(); j++) {
                if (s[i-1] == p[j-1] || p[j-1] == '.') {
                    dp[i][j] = dp[i-1][j-1];
                }
                
                if (p[j-1] == '*') {
                    if (p[j-2] != s[i-1] && p[j-2] != '.') {
                        dp[i][j] = dp[i][j-2];
                    } else {
                        // dp[i][j-2] => when a* is not counted
                        // dp[i][j-1] => when a* is counted for single `a`
                        // dp[i-1][j] => when a* is counted for multiple `a`
                        dp[i][j] = dp[i][j-2] || dp[i][j-1] || dp[i-1][j];    
                    }
                }
            }
        }
        
        return dp[s.size()][p.size()];
    }
};
