class Solution:
    def overlapInt(self, arr):
        n = len(arr)
        
        # Separate start and end times
        start = [interval[0] for interval in arr]
        end = [interval[1] for interval in arr]
        
        # Sort both
        start.sort()
        end.sort()
        
        i = 0  # pointer for start
        j = 0  # pointer for end
        
        curr_overlap = 0
        max_overlap = 0
        
        while i < n and j < n:
            # Since intervals are inclusive, use <=
            if start[i] <= end[j]:
                curr_overlap += 1
                max_overlap = max(max_overlap, curr_overlap)
                i += 1
            else:
                curr_overlap -= 1
                j += 1
        
        return max_overlap
