# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        R: Given a linked list return True if there is a linked list
        I: Fast slow ptrs
        D: Fast slow ptrs
        E: 
            1) ptr1 = head
                ptr2 = head .next
                while ptr2.next!=None:
                    if ptr1 == ptr2:



        """

        ptr1 = head
        if ptr1 == None:
            return False
        
        ptr2 = ptr1.next


        while ptr2 != None and ptr2.next != None:
            if ptr2 == ptr1:
                return True
            
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        
        return False









