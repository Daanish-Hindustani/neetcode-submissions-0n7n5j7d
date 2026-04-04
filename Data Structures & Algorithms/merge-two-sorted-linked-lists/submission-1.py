# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        R: Given Two SORTED Linkedlist merge them
        I: We have two ptrs one on the first list and the other on the second, merge the ptrs to a single head
        D: How to we handle duplicates? What happens at the end of a list if the other has more items?
        E:
            1) Crete ptrs for list 1 and list 2
            2) Adjust ptrs based on min 
            3) if ptr reachs end add next to second list
            4) return head
        """

        head = ListNode(None)
        res = head

        while list1 and list2:
            if list1.val<=list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            
            res = res.next
        
        if list1 == None:
            res.next = list2
        else:
            res.next = list1
        
        return head.next
            
