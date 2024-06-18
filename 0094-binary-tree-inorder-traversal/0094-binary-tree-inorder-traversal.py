# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
            return arr
        return inorder(root)