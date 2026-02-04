class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        merged = [intervals[0]]

        for start,end in intervals[1:]:
            if merged[-1][1] >= start:
                merged[-1][1] = max(end,merged[-1][1])
            else:
                merged.append([start,end])
        return merged