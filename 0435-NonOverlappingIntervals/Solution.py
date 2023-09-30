from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        count = 0
        previousInterval = intervals[0]
        for i in range (1, n):
            currentInterval = intervals[0]
            
            if currentInterval[0] < previousInterval[1]:
                count += 1
            else:
                previousInterval = currentInterval
        return count

"""
Time Complexity: O(n log n)
Space Complexity: O(n)
"""