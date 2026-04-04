# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast, slow = head, head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None 
        curr = slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 

        fst, snd = head, prev

        while snd:
            tpm1 = fst.next
            tpm2 = snd.next 

            fst.next = snd
            snd.next = tpm1

            fst = tpm1
            snd = tpm2
        