# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root is None:
            return None
        q=deque([(root,0)])
        mapper={}
        while q:
            node,line=q.popleft()
            mapper[line]=node.val
            if node.left:
                q.append((node.left,line+1))
            if node.right:
                q.append((node.right,line+1))

        for key,values in sorted(mapper.items()):
            ans.append(values)
        return ans