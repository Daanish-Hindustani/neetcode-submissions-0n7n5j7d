# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = {}

        curr = head
        i = 1
        while curr:
            nodes[i] = curr
            curr = curr.next
            i += 1

        lenght = len(nodes)
        j = lenght - n + 1
        
        if j == 1:
            head = head.next
        elif j == lenght:
            prev = nodes[j-1]
            next_node = None
            prev.next = next_node
        else:
            prev = nodes[j-1]
            next_node = nodes[j+1]
            prev.next = next_node
        
        return head