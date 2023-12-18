#User function Template for python3

class Solution:
    def nthPoint(self,n):
        mod = (10**9)+7
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1  # ways to reach the 1st stair
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] % mod + dp[i - 2] % mod) % mod
        return dp[n] 
