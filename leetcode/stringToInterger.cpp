/*
 * https://leetcode.com/problems/string-to-integer-atoi/
 */


#include<bits/stdc++.h> 

using namespace std; 

class Solution {    
public:
        
    int myAtoi(string str) {
        if (str.size() == 0) {
            return 0;
        }
        
        bool isNegativeInteger = false; 
        uint integer = 0; 
        
        for (int i = 0; i < str.size(); i++) {
            for (;str[i] == ' ' && i < str.size(); i++) {}
            
            if (str[i] == '+' || str[i] == '-') {
                isNegativeInteger = str[i] == '-' ? true: false;  
                i++;
            }
           
            for (; str[i] - '0' >= 0 && str[i] - '0' <= 9 && i < str.size(); i++) {
                if (INT_MAX / 10 < integer) {
                    return isNegativeInteger ? INT_MIN: INT_MAX; 
                }

                if (INT_MAX / 10 == integer && (str[i] - '0' == 9 && isNegativeInteger)) {
                    return INT_MIN;
                }  
                
                if (INT_MAX / 10 == integer && (str[i] - '0' > 7 && !isNegativeInteger)) {
                    return INT_MAX; 
                } 
                integer = integer * 10 + str[i] - '0';
            }

            return isNegativeInteger ? (-1 * integer): integer; 
        }

        return isNegativeInteger ? (-1 * integer): integer; 
    }
};
