from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList == [] or secondList == []:
            return []
        result =[]
        p1, p2 = 0, 0
        
        while p1 < len(firstList) and p2 < len(secondList):
            left = max(firstList[p1][0], secondList[p2],[0])
            right = min(firstList[p1][1], secondList[p2][1])
            
            if left < right:
                result.append([left, right])
            if firstList[p1][1] < secondList[p2][1]:
                i += 1
            else:
                j += 1
        return result

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""