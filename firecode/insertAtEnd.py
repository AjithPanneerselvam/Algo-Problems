"""
Inserting a Node at the End of a Singly Linked List
Write a function to insert a node at the end of a Singly Linked-List.
Click Use Me at the top to check the structure of Node.

Examples:
LinkedList: 1->2 , Head = 1

insertAtEnd(1) ==> 1->2->1
"""

class SinglyLinkedList:

    #method for inserting a new node at the end of a Linked List
    def insertAtEnd(self,data):

        if self.head == None:
            newNode = Node()
            newNode.setData(data)
            newNode.setNext(None)
            self.head = newNode
            return self.head

        traverse = self.head
        previous = None

        while (traverse != None):
            previous = traverse
            traverse = traverse.getNext()

        newNode = Node()
        newNode.setData(data)
        newNode.setNext(None)
        previous.setNext(newNode)
