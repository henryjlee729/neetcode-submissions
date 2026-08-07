"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()
        startPointer = 0
        endPointer = 0
        roomsInUse = 0
        maxRooms = 0
        while startPointer < len(intervals):
            if starts[startPointer] < ends[endPointer]:
                roomsInUse += 1
                maxRooms = max(maxRooms, roomsInUse)
                startPointer += 1
            else:
                roomsInUse -= 1
                endPointer += 1

        return maxRooms