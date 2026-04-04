# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for lst in lists:
            heapq.heappush(heap, NodeWrapper(lst))
        

        res = ListNode(0)
        curr = res

        while heap:
            min_node = heapq.heappop(heap)

            curr.next = min_node.node
            curr = curr.next

            if min_node.node.next:
                heapq.heappush(heap, NodeWrapper(min_node.node.next))

        return res.next


        
