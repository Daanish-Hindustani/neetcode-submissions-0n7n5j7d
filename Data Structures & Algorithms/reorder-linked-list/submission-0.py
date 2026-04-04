# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        R: Given a linkedlist, reorder it
        I: It looks we adjust ptrs between outter most values
        D: 2-> 10 10-> 4 4-> 8 8->6
        E:
            1) Move Ptr all the way to the right
            2->4->6->8->10
            2) left.next = right
            2->10<-8<-6<-4
            3) create a left and right ptr
            4) temp = left.next
            5) left.next = right
            6) left = temp
            7) temp = left.next
            8) right -> adjust will right .next == right
            9) if 
        """

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
            


        