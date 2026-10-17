class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        #size
        self.size = capacity
        self.cache = {}
        self.head = ListNode(-1, -1, None, None)
        self.tail = ListNode(-1, -1, None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, key):
        if key in self.cache:
            node = self.cache[key]
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            del self.cache[key]
    
    def add_node(self, key, value):
        new_node = ListNode(key, value)
        tail_prev = self.tail.prev
        tail_prev.next = new_node
        self.tail.prev = new_node

        new_node.next = self.tail
        new_node.prev = tail_prev
        self.cache[key] = new_node

        
            

    def get(self, key: int) -> int:
        print()
        if key in self.cache:
            val = self.cache[key].val
            self.remove(key)
            self.add_node(key,val)
            return val
        return -1


    def put(self, key: int, value: int) -> None:
        # update a keys values or add key val, if to big, evict LRU
        if key in self.cache:
            self.remove(key)
            self.add_node(key,value)
        else:
            self.add_node(key,value)
            if len(self.cache) > self.size:
                self.remove(self.head.next.key)
        
