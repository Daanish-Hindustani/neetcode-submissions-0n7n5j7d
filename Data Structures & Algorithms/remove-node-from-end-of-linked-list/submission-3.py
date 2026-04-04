# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head


        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head = prev
        curr = prev
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(n-1):
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
        
        curr = dummy.next
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev


