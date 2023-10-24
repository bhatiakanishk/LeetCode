from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        prev = nums[0]
        curr = max(nums[0], nums[1])
        
        for i in range (2, n):
            tmp = max(curr, nums[i] + prev)
            prev = curr
            curr = tmp
        
        return curr

"""
Space Complexity: O(1)
Time Complexity: O(n)
"""