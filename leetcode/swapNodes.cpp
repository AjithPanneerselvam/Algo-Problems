/*
* https://leetcode.com/problems/swap-nodes-in-pairs
* Time Complexity - O(n) 
* Space Complexity - O(1) 
*/

#include<bits/stdc++.h> 
using namespace std; 

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head; 
        }
    
        ListNode* temp = head; 
        int tmpVal; 
        while (temp != NULL && temp->next != NULL) {
            int tmpVal = temp->val;
            temp->val = temp->next->val;
            temp->next->val = tmpVal;
            temp = temp->next->next;
        }
        
        return head; 
    }
};
