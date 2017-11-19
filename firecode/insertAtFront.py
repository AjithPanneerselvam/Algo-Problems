"""
Insert a Node at the Front of a Linked List

Write a function to insert a node at the front of a Singly Linked-List

Examples:
LinkedList: 1->2 , Head = 1

insert_at_front(1) ==> 1->1->2
"""
class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    # Method for inserting a new node at the start of a Linked List
    def insert_at_front(self,data):
        node = Node()
        node.setData(data)
        node.setNext(self.head)
        self.head = node
        return self.head
