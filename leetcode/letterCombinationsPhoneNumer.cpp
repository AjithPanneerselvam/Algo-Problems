/*
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 *
 */

#include<bits/stdc++.h> 
using namespace std; 

class Solution {
public:
    map<char, string> getNumberToCharsMapping() {
        map<char, string> numberToChar = {
            make_pair('2', "abc"),
            make_pair('3', "def"),
            make_pair('4', "ghi"),
            make_pair('5', "jkl"),
            make_pair('6', "mno"),
            make_pair('7', "pqrs"),
            make_pair('8', "tuv"),
            make_pair('9', "wxyz"),
        };
        return numberToChar;
    }

    void findCombinations(vector<string>& result, map<char, string> numberToChar, string digits, int currentdigitIndex, int n, string combination) {
        if (currentdigitIndex == n) {
            result.push_back(combination);
            return;
        }

        string letters = numberToChar[digits[currentdigitIndex]];
        for (int i = 0; i < letters.size(); i++) {
            combination += letters[i];
            findCombinations(result, numberToChar, digits, currentdigitIndex + 1, n, combination);
            combination.pop_back();
        }
    } 
    
    vector<string> letterCombinations(string digits) {
        vector<string> result; 
        if(digits.size() == 0) {
            return result; 
        }
        
        map<char, string> numberToChar = getNumberToCharsMapping();
        string combination;
        findCombinations(result, numberToChar, digits, 0, digits.size(), combination);
        return result;
    }
};
