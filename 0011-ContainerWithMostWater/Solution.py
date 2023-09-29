from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            h = min(height[left], height[right])  # Height of the container
            w = right - left  # Width of the container
            area = h * w  # Area of the container
            
            max_area = max(max_area, area)  # Update the maximum area
            
            # Move the pointer with the smaller height towards the center
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

"""
Space Complexity: O(n)
Time Complexity: O(1)
"""