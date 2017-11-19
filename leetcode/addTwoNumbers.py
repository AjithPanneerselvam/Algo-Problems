"""
https://leetcode.com/problems/add-two-numbers/#/description

Time Complexity - O(n)
Space Complexity - O(n)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        firstItr = 1
        carry = 0
        list1 = l1
        list2 = l2

        while(list1!= None and list2 != None):
            digit = (list1.val + list2.val + carry) % 10
            carry = (list1.val + list2.val + carry) / 10

            temp = ListNode(digit)

            if firstItr:
                head = temp
                prev = temp
                firstItr = 0
                list1 = list1.next
                list2 = list2.next

                continue

            prev.next = temp
            prev = temp

            list1 = list1.next
            list2 = list2.next

        while(list1 != None):
            digit = (list1.val + carry) % 10
            carry = (list1.val + carry) / 10
            temp = ListNode(digit)
            prev.next = temp
            prev = temp
            list1 = list1.next

        while(list2 != None):
            digit = (list2.val + carry) % 10
            carry = (list2.val + carry) / 10
            temp = ListNode(digit)
            prev.next = temp
            prev = temp
            list2 = list2.next

        if carry > 0:
            temp = ListNode(carry)
            prev.next = temp


        temp.next = None

        return head
