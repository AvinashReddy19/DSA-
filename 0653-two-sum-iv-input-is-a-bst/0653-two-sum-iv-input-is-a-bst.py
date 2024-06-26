# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
		# Store k - vals we come across in our vals dict (O(1) lookup).
        vals = {}
        
        def helper(node):
		    # If we run out of nodes on this path we know there was no val, False.
            if not node:
                return False
			# If we come across a val needed to make the sum, return True.
            if node.val in vals:
                return True
			# If none of the above, add k - node.val to vals.
            vals[k - node.val] = True
			# Return if we were able to find a path in either subtree.
            return helper(node.left) or helper(node.right)
        
        return helper(root)