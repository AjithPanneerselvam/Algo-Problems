/*
* https://leetcode.com/problems/generate-parentheses 
*/

#include<bits/stdc++.h> 
using namespace std; 


class Solution {
public:
    void findAllCombinations(vector<string>& combinations, string paranthesis, int i, int unclosed, int n) {
        if (i == n-1) {
            paranthesis += "(";
            for (int j = 0; j < unclosed + 1; j++) {
                paranthesis += ")";
            }

            combinations.push_back(paranthesis);
            return;
        }

        paranthesis += "(";
        findAllCombinations(combinations, paranthesis, i + 1, unclosed + 1, n);
        
        for (int j = 0; j < unclosed + 1; j++) {
            paranthesis += ")";
            findAllCombinations(combinations, paranthesis, i + 1, unclosed - j, n);
        }
    }
    
    vector<string> generateParenthesis(int n) {
        vector<string> combinations;
        if (n == 0) {
            return vector<string>{""}; 
        }
        
        findAllCombinations(combinations, "", 0, 0, n); 
        return combinations;
    }
};
