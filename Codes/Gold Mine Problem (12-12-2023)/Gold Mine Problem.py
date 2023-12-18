# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # code here
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            dp[i][0] = M[i][0]

        for j in range(1, m):
            for i in range(n):
                move_up = dp[i - 1][j - 1] if i - 1 >= 0 else 0
                move_right = dp[i][j - 1]
                move_down = dp[i + 1][j - 1] if i + 1 < n else 0

                dp[i][j] = M[i][j] + max(move_up, move_right, move_down)

        max_gold = max(dp[i][-1] for i in range(n))
        return max_gold
