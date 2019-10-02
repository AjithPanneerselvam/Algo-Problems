#include<bits/stdc++.h> 

using namespace std; 

// Definition for singly-linked list.
 struct ListNode {
 int val;
 ListNode *next;
 ListNode(int x) : val(x), next(NULL) {}
 };
 

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* head = NULL; 
        ListNode* result = NULL; 
        ListNode* small = NULL;
            
        while(l1 != NULL && l2 != NULL) {
            if (l1->val <= l2->val) {
                small = l1; 
                l1 = l1 -> next; 
            } else {
                small = l2;
                l2 = l2 -> next; 
            }
            
            if (result != NULL) {
                result->next = small;
                result = result -> next; 
            } else {
                result = small;
                head = small; 
            }
        }
        
        while (l1 != NULL) {
            if (result != NULL) {
                result -> next = l1; 
                result = result -> next;
            } else {
                result = l1; 
                head = l1; 
            }
            cout<<result->val<<" ";
            l1 = l1 -> next; 
        }
        
        while (l2 != NULL) {
            if (result != NULL) {
                result -> next = l2; 
                result = result -> next; 
            } else {
                result = l2; 
                head = l2; 
            }
            
            l2 = l2 -> next; 
        }
        
        return head; 
    }
};
