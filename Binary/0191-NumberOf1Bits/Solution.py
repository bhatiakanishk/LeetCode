class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        mask = 1
        
        for _ in range(32):  # Since the input is a binary string of length 32
            if n & mask:
                count += 1
            mask <<= 1
        
        return count

"""
Time Complexity: O(1)
Space Complexity: O(1)
"""