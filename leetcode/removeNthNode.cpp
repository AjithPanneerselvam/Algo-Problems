
#include<bits/stdc++.h>

using namespace std; 

 struct ListNode {
 int val;
 ListNode *next;
 ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
         ListNode* leadPointer = head; 
         for (int i =  0; i < n; i++) {
             leadPointer = leadPointer -> next; 
         }
        
        ListNode* nthNode = head;
        ListNode* prev = head;
        while (leadPointer != NULL) {
            prev = nthNode; 
            nthNode = nthNode -> next; 
            leadPointer = leadPointer -> next; 
        }
        
        if (nthNode == head) {
            head = head -> next; 
        } else {
            prev -> next = nthNode -> next;
        }
        
        return head;
    }
};
