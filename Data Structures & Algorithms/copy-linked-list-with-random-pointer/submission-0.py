"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        R: Given a Linked List where each node has a next ptr and a random ptr, create a deep copy
        I: We can easily copy the linkedlist with the next ptrs included, additionally we can
            do a second pass and copy the rand ptr too.
        D: How do we know the assoiation between the randoptr to a node in the orginal set and the 
            correct node we need to assign to rand ptr in the copy?
        E: 
            1) Create a hash of each node -> map old nodes to new nodes
            2) Iterate through these nodes agaian and get the correct refs for the next and random
                Through the hash
        """

        oldToNew = { None: None}

        curr = head
        while curr:
            newNode = Node(curr.val)
            oldToNew[curr] = newNode
            curr = curr.next
        
        curr = head
        while curr:
            newNode = oldToNew[curr]
            newNode.next = oldToNew[curr.next]
            newNode.random = oldToNew[curr.random]
            curr = curr.next
        

        return oldToNew[head]














