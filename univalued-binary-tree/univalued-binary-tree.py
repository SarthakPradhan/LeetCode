# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True
        
        if root.left:
            left_bool = (root.val==root.left.val)
        else: left_bool = True
        
        if root.right:
            right_bool = (root.val==root.right.val)
        else: right_bool = True
        
        tot_bool = left_bool and right_bool
        
        return (tot_bool and self.isUnivalTree(root.left) and self.isUnivalTree(root.right))
        