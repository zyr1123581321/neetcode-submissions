class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        mergeInt = [intervals[0]]

        for i in range(1, len(intervals)):
            a1, b1 = intervals[i][0], intervals[i][1]
            a0, b0 = mergeInt[-1]
            if a1 <= b0:
                mergeInt[-1] = [a0, max(b0, b1)]
            else: 
                mergeInt.append([a1, b1])
        
        return mergeInt
