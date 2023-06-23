from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        right_prod = 1
        # Calculate the product of all elements to the left of each element
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        # Calculate the product of all elements to the right of each element and multiply with the left product
        for i in range(n-1, -1, -1):
            result[i] *= right_prod
            right_prod *= nums[i]
        return result

"""
Space Complexity: O(1)
Time Complexity: O(n)
"""