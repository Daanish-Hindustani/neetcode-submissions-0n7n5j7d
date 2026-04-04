# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        R: Given a linked list reverse it
        I: We need to use 3 ptrs to reverse a linked list
        D: ptrs
        E:
            1) ptr1, ptr2, ptr3
            2) ptr2.next = ptr1
               ptr1 = pt2
               ptr2 = ptr3
               ptr3 = ptr.next
            3) when ptr is null, return ptr2 and set ptr2.next = ptr1
        """
        
        ptr1 = None
        ptr2 = head

        while ptr2!=None:
            temp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = temp
        
        return ptr1
    














