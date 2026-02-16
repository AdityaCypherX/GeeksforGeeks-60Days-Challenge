#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):

        # code here
        n = len(arr)
        if M == 0 or n == 0:
            return 0
        
        # Sort the array
        arr.sort()
        
        # If students are more than packets
        if M > n:
            return -1
        
        min_diff = float('inf')
        
        # Check each subarray of size m
        for i in range(n - M + 1):
            diff = arr[i + M - 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                
        return min_diff
