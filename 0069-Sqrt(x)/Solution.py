class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid
            if squared == x:
                return mid
            elif squared < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

"""
Space Complexity: O(1)
Time Complexity: O(log n)
"""