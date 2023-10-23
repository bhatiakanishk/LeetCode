from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # Convert list to set for O(1) lookups
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string can be segmented
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
                    
        return dp[len(s)]

"""
n = Length of input string
m = Average Length of words in dictionary
Time Complexity: O(n^2 * m)
Space Complexity: O(n + m)
"""