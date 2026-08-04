class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        result.append(intervals[0])
        for index in range(1, len(intervals)):
            currentInterval = intervals[index]
            lastMergedInterval = result[-1]
            if currentInterval[0] <= lastMergedInterval[1]:
                lastMergedInterval[1] = max(lastMergedInterval[1], currentInterval[1])
            else:
                result.append(currentInterval)

        return result