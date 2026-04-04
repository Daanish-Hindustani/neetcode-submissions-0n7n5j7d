
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = res[-1]
            curr = intervals[i]

            if prev[1] < curr[0]:  
                res.append(curr)
            else:  
                prev[1] = max(prev[1], curr[1])

        return res