"""
# Salesforce

Looping Lists : Space complexity O(1)

Given a Singly Linked-List, implement a method to check if the list has cycles. The Space complexity should be O(1).
If there is a cycle, return true. Otherwise, return false. Empty lists should be considered non-cyclic.
Be sure to click Use Me to check Node's structure.

Examples:
1->2->3->4->1 ==> True

1->2->3->4 ==> False
"""

class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    def is_cyclic(self):
        rabbit = self.head.next
        tortoise = self.head

        while(rabbit != None):
            if rabbit.next == None:
                return False

            if rabbit == tortoise:
                return True

            rabbit = rabbit.next.next
            tortoise = tortoise.next

        return False
