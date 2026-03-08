# 3. Given a list of intervals, where each interval is represented as a list [start, end], merge all
# overlapping intervals and return a new list of the non overlapping intervals that cover all the
# intervals in the input.
# Example:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]


intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()
merged = []

for start, end in intervals:
    if merged == []:
        merged.append([start,end])
    else:
        last = merged[-1]
        
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            merged.append([start,end])

print(merged)