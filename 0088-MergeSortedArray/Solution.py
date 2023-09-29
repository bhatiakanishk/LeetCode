from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m -1 # Pointer to end of nums1
        p2 = n - 1  # Pointer to end of nums2
        p3 = m + n - 1 # Pointer to end of nums 1 for merged result
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1
            
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p3 -= 1
            p2 -= 1

"""
Space Complexity: O(1)
Time Complexity: O(m + n)
"""