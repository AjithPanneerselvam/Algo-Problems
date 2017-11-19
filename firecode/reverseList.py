"""
Microsoft

Reverse a Singly Linked List
Given a singly linked list, write a method to perform In-place reversal.

Example:
1->2->3 ==> 3->2->1
"""

class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    def reverse(self):
        previous = None
        traverse = self.head

        while (traverse != None):
            temp = traverse.getNext()
            traverse.setNext(previous)
            previous = traverse
            traverse = temp

        self.head = previous
