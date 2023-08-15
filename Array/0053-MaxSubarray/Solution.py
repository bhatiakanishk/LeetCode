from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = []
        arr.append(nums[0])
        maxSum = arr[0]
        for i in range (1, len(nums)):
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            if arr[i] > maxSum:
                maxSum = arr[i]
        return maxSum

"""
Space Complexity: O(n)
Time Complexity: O(n)
"""