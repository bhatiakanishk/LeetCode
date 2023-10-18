from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        numCoins = len(coins)
        
        minCoins = [amount + 1] * (amount + 1)
        minCoins[0] = 0
        
        for i in range(amount + 1):
            for coin in coins:
                if coin <= i:
                    minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)
        
        if minCoins[amount] == amount + 1:
            return -1
        
        return minCoins[amount]

"""
Time Complexity: O(amount * numCoins)
Space Complexity: O(amount)
"""