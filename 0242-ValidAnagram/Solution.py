class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_dict = {}
        for i in range(len(s)):
            count_dict[s[i]] = count_dict.get(s[i], 0) + 1
            count_dict[t[i]] = count_dict.get(t[i], 0) - 1
        for count in count_dict.values():
            if count != 0:
                return False
        return True

"""
Space Complexity: O(1)
Time Complexity: O(n)
"""