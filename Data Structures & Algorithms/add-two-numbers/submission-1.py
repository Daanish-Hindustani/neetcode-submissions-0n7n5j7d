# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        R: Given Two Linked list(might have different lenghts), and that are stored in reverse fashion, return the sum of the two linkedlists
        I: The linked lists start at the least significant digit. We just need to add at each step and use a carry over
        D: What happends when the Linkedlist is null for one?
        E: 1) Start at the head and move to the right for each linkedlist
           2) The sum should be held in a new node. 
           3) If there is carry over user a temp val to hold it and add to the next node
           4) If on of the linked list ended while the other is avalible just retiurn those node, and add the carry over
        """

        carry_over = 0
        dummy = ListNode(None)
        curr = dummy

        while l1 and l2:
            res = l1.val + l2.val + carry_over
            #Calc carry over 
            temp = str(res)
            
            if len(temp) > 1:
                carry_over = int(temp[0])
                res = int(temp[1])
            else:
                carry_over = 0

            new_node = ListNode(res)
            curr.next = new_node
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        ptr = None
        if l1:
            ptr = l1
        elif l2:
            ptr = l2
        else:
            ptr = None

        while ptr:
            res = ptr.val + carry_over
            temp = str(res)
            if len(temp) > 1:
                carry_over = int(temp[0])
                res = int(temp[1])
            else:
                carry_over = 0

            new_node = ListNode(res)
            curr.next = new_node
            curr = curr.next
            ptr = ptr.next
        
        if carry_over != 0:
            new_node = ListNode(carry_over)
            curr.next = new_node
            curr = curr.next


        
        return dummy.next

        

