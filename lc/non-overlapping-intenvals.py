# https://leetcode.com/problems/non-overlapping-intervals/submissions/
# Given a collection of intervals, find the minimum number of intervals
# you need to remove to make the rest of the intervals non-overlapping.
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

def eraseOverlapIntervals(self, intervals):
    count = 0
    if len(intervals) in [0, 1]:
        return count
    sorted_intervals = sorted(intervals, key=lambda i: i[0])
    prev = sorted_intervals[0][1]
    for index, interval in enumerate(sorted_intervals[1:]):
        if interval[0] < prev:
            count += 1
            prev = min(interval[1], prev)
        else:
            prev = interval[1]
    return count


def eraseOverlapIntervals1(self, intervals):
    count = 0
    if len(intervals) in [0, 1]:
        return count
    sorted_intervals = sorted(intervals, key=lambda i: i[1])
    prev = sorted_intervals[0][1]
    for index, interval in enumerate(sorted_intervals[1:]):
        if interval[0] < prev:
            count += 1
        else:
            prev = interval[1]
    return count

