# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        R: Given a linkedlist reorder the linkedlist
        I: The other edges are reassigned then the ptrs move inwards and the process repeats
            - the outside nodes are adjusted to pt to each other
            - ptrs move inwards
        D: How do we adjust the ptrs?
        E: ADJUST THE DIRECTION OF THE PTRS ON THE RIGHT HALF and move towards each other
            1) Use fast slow ptrs to reach the middle
            2) Reverse the right half of the linked list
            3) Iterate from the on both linked list and adjust ptrs
        """

        # Find middle

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half

        ptr1 = None
        ptr2 = slow.next
        slow.next = None

        while ptr2:
            temp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = temp
        
        # Combine

        first, second = head, ptr1

        while second:
            temp1 = first.next 
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        




























