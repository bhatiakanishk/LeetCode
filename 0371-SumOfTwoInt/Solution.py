class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b != 0:
            carry = a & b
            
            a = (a ^ b) & mask
            
            b = (carry << 1) & mask      
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
        
        return a

"""
Time Complexity: O(1)
Space Complexity: O(1)
"""