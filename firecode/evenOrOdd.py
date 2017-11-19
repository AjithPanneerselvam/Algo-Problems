"""
Oracle
Time-Complexity - O(n)
Space-Complexity - O(1)

Even or Odd?
Given a Singly Linked-List, check whether its length is even or odd in a single pass.

Example:
1->2->3->4 ==> True

1->2->3->4->5 ==> False
"""
class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    def is_list_even(self):
        if self.head == None:
            return True
        elif self.head.getNext() == None:
            return False

        fast = self.head

        while (fast != None):
            if fast.getNext() == None:
                return False

            fast = fast.getNext()
            fast = fast.getNext()

        return True
