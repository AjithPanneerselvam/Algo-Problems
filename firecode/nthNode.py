"""
Find the "Nth from the end" Node in a List
Time Complexity - O(n)
Space Complexity - O(n)

Given a Singly Linked-List, write a function that returns the "Nth from the end" node of the list.

Example:
1->2->3->4->5->6, n=2 ==> 5

Note: Check out Use Me section to find out Node's structure. Your solution should return the entire node, not just it's data.
"""


def find_nth_node_from_end(self, n):
    if self.head == None or n < 1:
        return None

    stack = list()
    head = self.head
    lenList = 0

    while(head != None):
        stack.append(head)
        head = head.getNext()
        lenList += 1

    if lenList < n:
        return None

    i = 1
    while(i <= n):
        NthNode = stack.pop()
        i += 1

    return NthNode
