from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {} # Dictionary to keep count of elements
        result = [] # Array to store result
        
        # Populate dictionary with nums1
        for num in nums1:
            # If number already exists in dictionary, increase its count
            if num in count:
                count[num] += 1
            # If a new number is added in dictionary, set count to 1
            else:
                count[num] = 1
        
        # Iterate through nums2 to find intersection elements
        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1
        return result

"""
N: length of nums1
M: length of nums2
Time Complexity: O(N + M)
Space Complexity: O(min(N, M))
"""