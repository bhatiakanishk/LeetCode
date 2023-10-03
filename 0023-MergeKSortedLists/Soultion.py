from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Initialize a min-heap to store the (value, node) pairs.
        min_heap = []
        
        # Push the first node from each list into the min-heap.
        for i, linked_list in enumerate(lists):
            if linked_list:
                heapq.heappush(min_heap, (linked_list.val, i))
                lists[i] = linked_list.next
        
        # Initialize a dummy node as the head of the merged list.
        merged_head = ListNode()
        current = merged_head
        
        # Continue until the min-heap is empty.
        while min_heap:
            # Pop the smallest (value, index) pair from the min-heap.
            val, index = heapq.heappop(min_heap)
            
            # Append the value to the merged list.
            current.next = ListNode(val)
            current = current.next
            
            # If there are more nodes in the corresponding list, push the next node.
            if lists[index]:
                heapq.heappush(min_heap, (lists[index].val, index))
                lists[index] = lists[index].next
        
        # Return the merged sorted linked list (excluding the dummy head).
        return merged_head.next