# https://leetcode.com/problems/merge-intervals/submissions/
#Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]

def merge(intervals):
    output = []
    for interval in sorted(intervals, key=lambda i: i[0]):
        if output and output[-1][1] >= interval[0]:
            output[-1][1] = max(interval[1], output[-1][1])
        else:
            output.append(interval)
    return output


input = [[1,3],[2,6],[8,10],[15,18]]
print(merge(input))
