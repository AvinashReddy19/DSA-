# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        levels=[]
        queue= deque([root])
        while queue:
            cur_level_size=len(queue)
            curr_lvl=[]
            for _ in range(cur_level_size):
                front=queue.popleft()
                curr_lvl.append(front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            levels.append(curr_lvl)
        return levels