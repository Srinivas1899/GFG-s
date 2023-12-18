#User function Template for python3
class Solution:
    
    def findMaxSum(self,arr, n):
        # code here
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
 
        dp = [0] * n
 
        # Base cases
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
 
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
 
        return max(dp[n - 1], dp[n - 2])
