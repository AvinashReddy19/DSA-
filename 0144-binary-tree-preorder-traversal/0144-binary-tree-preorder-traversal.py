# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        def preorder(node):
            if node is None:
                return 
            arr.append(node.val)
            preorder(node.left)
            preorder(node.right)
            return arr
        return preorder(root)
        
        