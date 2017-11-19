"""
Find the Middle Node of a Singly Linked-List
Time Complexity - O(n)
Space Complexity - O(1)

Given a Singly Linked-List, write a function to find and return the middle node of the list. Try and limit the runtime complexity to O(n) and space complexity to O(1).

Examples:
1 ==> 1

1->2 ==> 1

1->2->3->4 ==> 2

1->2->3->4->5 ==> 3
"""


class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    def find_middle_node(self):
        if self.head.next == None:
            return self.head

        rabbit = self.head.next
        tortoise = self.head

        while(True):
            if rabbit == None:
                return tortoise

            if rabbit.next == None:
                return tortoise

            tortoise = tortoise.next
            rabbit = rabbit.next.next
