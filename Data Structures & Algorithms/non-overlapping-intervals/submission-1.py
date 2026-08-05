class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals = 0
        previousEnd = intervals[0][1]
        for index in range(1, len(intervals)):
            currentStart = intervals[index][0]
            currentEnd = intervals[index][1]
            if currentStart < previousEnd:
                removals += 1
            else:
                previousEnd = currentEnd

        return removals