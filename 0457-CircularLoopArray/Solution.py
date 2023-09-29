from typing import List
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)        
        def next_index(current_index):
            return (current_index + nums[current_index]) % n
        for i in range(n):
            if nums[i] == 0:
                continue
            slow = i
            fast = i
            # Check if the cycle is valid (either all positive or all negative)
            while nums[slow] * nums[next_index(slow)] > 0 and nums[fast] * nums[next_index(fast)] > 0:
                slow = next_index(slow)
                fast = next_index(next_index(fast))
                if slow == fast:
                    if slow == next_index(slow):
                        break  # Cycle of size 1, ignore it
                    return True  # Found a valid cycle
            # Mark the current cycle as invalid
            slow = i
            while nums[slow] * nums[next_index(slow)] > 0:
                tmp = next_index(slow)
                nums[slow] = 0  # Mark the current index as visited
                slow = tmp
        return False  # No valid cycle found

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""