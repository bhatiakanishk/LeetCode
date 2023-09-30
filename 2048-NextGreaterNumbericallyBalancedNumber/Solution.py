class Solution:
    def isNumericallyBalanced(self, num: int) -> bool:
        num_str = str(num)
        for digit in num_str:
            count = num_str.count(digit)
            if count != int(digit):
                return False
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        while True:
            if self.isNumericallyBalanced(n):
                return n
            n += 1

"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""