# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        R: Given a Linked List and a val n, remove the nth node STARTING from the END of the linked List
        I: REVERSE !!! REVERSE !!!, We can reverse the list then remove then reverse again
        D: What happens if the head is the node that is removed? how to return the head?
        E: 
            1) Reverse the linkedlist
            2) Remove the nth node
            3) reverse the list again
            4) Return the head
        """

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
        #1,2,3,4,5 n=2
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
        
        #Reverse List AGAIN
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        
        return first


        



