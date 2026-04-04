# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        R: Given Two sorted Linkedlist we need to merge both and return head

        I: Use Ptr to iterate through both lists with 3 conditions
            1) less than 
            2) greater than
            3) equal
            Adjust ptrs based on that

        D: We have a ptr1, ptr2, 
            if ptr1 > ptr2 -> add ptr2 -> move ptr2 += 1
            if ptr1 < ptr2 -> add ptr 1 -> move ptr1 += 1
            if ptr1 == ptr2 -> add ptr and add ptr -> move both +=1
            Finally if either ptr1 or ptr2 is null .next is with ptr 1 or 2
        E: Above

        """

        dummy = ListNode(0)  # Dummy head
        res = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next

        # Attach the remaining nodes
        res.next = list1 if list1 else list2

        return dummy.next





