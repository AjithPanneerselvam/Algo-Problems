"""
Oracle
Delete the Node at a Particular Position in a Linked List
Time Complexity - O(n)
Space Complexity - O(1)

Given a Singly Linked-List, implement a method to delete the node that contains the same data as the input data.

Example:
delete(1->2->3->4,3) ==> 1->2->4
"""


class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    #method for deleting a node having a certain data
    def delete(self,data):
        if self.head == None:
            return self.head

        current = self.head

        while(current != None):
            if current.data == data and self.head == current:
                self.head = current.next
                break
            elif current.data == data:
                previous.next = current.next
                break
            else:
                previous = current
                current = current.next
