class TimeMap:
    """
    R: Given some data structure. where each element is has a key and a list of values at specifc time stamps
    Build out func set which sets a value for a given key at a specic ts. And fet which get the most
    Recent value.
    I: Use a default dict to store the key value pairs


    """

    def __init__(self):
        self.obj = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.obj:
            self.obj[key] = []
        
        self.obj[key].append([value, timestamp])
    

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.obj.get(key, [])

        l,r = 0, len(values)-1
        while l<=r:
            mid = (l+r)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
            
            
        return res

        
