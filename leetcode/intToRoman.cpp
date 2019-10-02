/*
 * https://leetcode.com/problems/integer-to-roman
 * Time Complexity - log(n), base - 10
 * Space Complexity - O(1) - constant space for map 
 */

#include<bits/stdc++.h> 
using namespace std; 

// "a" * 3
string operator*(std::string s, size_t count)
{
    std::string ret;
    for(size_t i = 0; i < count; ++i)
    {
        ret = ret + s;
    }
    return ret;
}

class Solution {
public:
    vector<pair<int, string>> getIntToRomanMapping() {
        vector<pair<int, string>> intToRoman = {
            make_pair(1000, "M"),
            
            make_pair(900, "CM"),
            make_pair(500, "D"),
            make_pair(400, "CD"),
            make_pair(100, "C"),
            
            make_pair(90, "XC"),
            make_pair(50, "L"),
            make_pair(40, "XL"),
            make_pair(10, "X"),
            
            make_pair(9, "IX"),
            make_pair(5, "V"),
            make_pair(4, "IV"),
            make_pair(1, "I")
        };
                
        return intToRoman; 
    }
    
    string intToRoman(int num) {
        vector<pair<int, string>> intToRoman = getIntToRomanMapping();         
        string roman; 
        int times = 0; 
        
        for (vector<pair<int, string>>::iterator it = intToRoman.begin(); it != intToRoman.end(); ++it) {
            times = num / it->first; 
            if (times < 1) {
                continue;
            } 

            roman += it->second * times; 
            num = num % it->first; 
            if (num == 0) {
                return roman;
            }
        }
        
        return roman;
    }
};
