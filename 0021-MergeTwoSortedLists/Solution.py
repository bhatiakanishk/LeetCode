from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        p1 = list1
        p2 = list2
        
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        current.next = p1 if p1 is not None else p2
        
        return dummy.next

"""
M: length of list1
N: length of list2
Space Complexity: O(1)
Time Complexity: O(min(M, N))
"""