/*
 * https://leetcode.com/problems/valid-parentheses/

 Time Complexity - O(n)
 Space Complexity - O(n)
*/

#include <stack>

class Solution {
    bool isPresent(char brackets[], int n, char c){
        for (int i = 0; i < n; i++){
            if (brackets[i] == c) {
                return true;
            }
        }
        return false;
    }

public:
    bool isValid(string s) {
        stack<char> st;
        char openingBrackets[] = {'(', '{', '['};
        int n = 3;
        char ch;
        map<char, char> pairs;
        pairs['('] = ')';
        pairs['{'] = '}';
        pairs['['] = ']';

        for (int i = 0; i < s.length(); i++){
            if (isPresent(openingBrackets, n, s[i])) {
                st.push(s[i]);
            } else {
                if (st.size() == 0) {
                    return false;
                }

                ch = st.top();
                st.pop();
                if (pairs[ch] != s[i]){
                    return false;
                }
            }
        }

        if (st.size() != 0) {
            return false;
        }

        return true;
    }
};
