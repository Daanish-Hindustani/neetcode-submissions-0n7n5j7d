"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        res = []

        for interval in intervals:
            if not res:
                res.append([interval.start, interval.end])
            else:
                if interval.start < res[-1][1]:
                    return False
                
                else:
                    res.append([interval.start, interval.end])
        
        return True