class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1  # 1 way to reach the first step
        dp[2] = 2  # 2 ways to reach the second step
        
        # Loop through the rest of the steps, updating each one based on the sum of the previous two steps
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n]

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""