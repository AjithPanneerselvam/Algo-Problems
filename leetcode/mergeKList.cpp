/*
 * https://leetcode.com/problems/merge-k-sorted-lists  
 * Time Complexity - O(m * n), where m is the number of lists and n is the average number of nodes in each list 
 * Space Complexity - O(1)
 */

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
    ListNode* mergeKLists(vector<ListNode*>& lists) {   
        ListNode* previousNode = NULL;
        ListNode* head = NULL; 
        
        for(;;) {
            ListNode* currentNode = NULL; 
            
            int i = 0, minNode; 
            for (;i < lists.size(); i++) {
                if (lists[i] != NULL) {
                    currentNode = lists[i];
                    break;
                }
            }
            
            if (currentNode == NULL) {
                break; 
            }
            
            minNode = i; 
            for (;i < lists.size(); i++) {
                if (lists[i] != NULL && lists[i]->val < currentNode->val) {
                    currentNode = lists[i]; 
                    minNode = i; 
                } 
            }
            
            if (head == NULL) {
                head = currentNode; 
            } else {
                previousNode->next = currentNode;
            }
            
            lists[minNode] = lists[minNode]->next;
            previousNode = currentNode; 
        }
    
        return head; 
    }
};

