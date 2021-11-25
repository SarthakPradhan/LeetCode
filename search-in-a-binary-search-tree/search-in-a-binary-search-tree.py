# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(root,val):
            if not root: return None
            if val == root.val:
                return root

            l= traverse(root.left,val) 
            r = traverse(root.right,val)
            
            if l:return l
            elif r:return r
            else:None
                
        return traverse(root,val)