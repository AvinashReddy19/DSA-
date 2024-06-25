# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum=0
    def bstToGst(self, node: TreeNode) -> TreeNode:
        if node:
            self.bstToGst(node.right)
            self.sum+=node.val
            node.val=self.sum
            self.bstToGst(node.left)
        return node