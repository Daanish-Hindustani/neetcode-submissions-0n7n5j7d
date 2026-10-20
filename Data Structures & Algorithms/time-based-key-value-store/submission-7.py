class TimeMap:

    def __init__(self):
        self.kv_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append((timestamp, value))


        

    def get(self, key: str, timestamp: int) -> str:

        res = ""

        if key not in self.kv_store:
            return ""
        
        temp = self.kv_store[key]
        
        l,r = 0, len(temp)-1

        while l<=r:
            mid = (l+r)//2

            if temp[mid][0] <= timestamp:
                res = temp[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
