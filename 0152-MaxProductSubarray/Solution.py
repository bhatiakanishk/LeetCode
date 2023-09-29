from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxProduct = nums[0]
        minProduct = nums[0]
        overallMax = nums[0]
        
        for i in range (1 , len(nums)):
            if nums[i] < 0:
                maxProduct, minProduct = minProduct, maxProduct
            
            maxProduct = max(nums[i], maxProduct * nums[i])
            minProduct = min(nums[i], minProduct * nums[i])
            
            overallMax = max(overallMax, maxProduct)
        return overallMax

"""
Space Complexity: O(1)
Time Complexity: O(n)
"""