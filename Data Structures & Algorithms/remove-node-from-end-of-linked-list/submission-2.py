# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first = None
        second = head

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        prev = None
        ptr = first
        second = ptr

        for i in range(n-1):
            prev = ptr
            ptr = ptr.next
        
        if prev == None:
            second = ptr.next
            ptr.next = None
        
        else:
            prev.next = ptr.next
            ptr.next = None
        
        first = None

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        return first


