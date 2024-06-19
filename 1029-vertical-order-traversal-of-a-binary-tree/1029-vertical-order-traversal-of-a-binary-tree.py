# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapper = defaultdict(list)
        def dfs(x,y,node):
            if node is None:
                return
            dfs(x-1,y+1,node.left)
            dfs(x+1,y+1,node.right)
            mapper[(x,y)].append(node.val)
        
        dfs(0,0,root)
        output=[]
        old = float('-inf')
        for key,v in sorted(mapper.items()):
            if key[0]!=old:
                output.append([])
            output[-1].extend(sorted(v))
            old=key[0]
        return output