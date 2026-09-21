class TimeMap:

    def __init__(self):
        self.kv_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        kv_list = []
        if key in self.kv_store:
            kv_list = self.kv_store[key]
        else:
            return None
        

        l,r = 0, len(kv_list) - 1

        while l<=r:
            mid = (l+r)//2

            if kv_list[mid][0] == timestamp:
                return kv_list[mid][1]
            
            elif kv_list[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        return kv_list[r][1]
            
        