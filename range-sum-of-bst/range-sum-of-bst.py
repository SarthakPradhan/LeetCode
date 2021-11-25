# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def sumNodes(root):
            
            if not root: return 0
            
            if root.val<=high and root.val>=low:
                val_root = root.val
            else:
                val_root = 0
                
            return val_root+sumNodes(root.left)+sumNodes(root.right)
        
        return sumNodes(root)