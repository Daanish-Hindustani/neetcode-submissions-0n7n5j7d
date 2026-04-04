# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        
        
        first = None
        second = slow.next
        slow.next = None 

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        
        second = first
        first = head 
        
        while second and first:
            temp = second.next
            temp2 = first.next

            first.next = second
            second.next = temp2

            first = temp2
            second = temp
        
        




