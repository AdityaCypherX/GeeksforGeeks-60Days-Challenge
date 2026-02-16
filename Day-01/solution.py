class Solution:
    def minTime (self, arr, k):
        # code here
        if not arr:
            return 0
        low=max(arr)
        high=sum(arr)
        def is_possible(max_time):
            painters = 1
            current_sum = 0
            
            for board in arr:
                if current_sum + board <= max_time:
                    current_sum += board
                else:
                    painters += 1
                    current_sum = board
                    
                    if painters > k:
                        return False
            
            return True
        
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if is_possible(mid):
                result = mid
                high = mid - 1   # try smaller maximum time
            else:
                low = mid + 1    # increase allowed time
        
        return result
