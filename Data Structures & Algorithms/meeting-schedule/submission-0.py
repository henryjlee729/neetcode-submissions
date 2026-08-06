"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
       
        intervals.sort(key=lambda x: x.start)
        for index in range(1, len(intervals)):            
            previousMeeting = intervals[index - 1]
            currentMeeting = intervals[index]
            if currentMeeting.start < previousMeeting.end:
                return False

        return True