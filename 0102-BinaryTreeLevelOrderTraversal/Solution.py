from collections import deque
from typing import List, Optional

# Define binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        queue = deque()
        
        queue.append(root)
        
        while queue:
            level = []
            levelSize = len(queue)
            
            for i in range(levelSize):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        return result

"""
Time Complexity: O(N)
Space Complexity: O(N)
"""