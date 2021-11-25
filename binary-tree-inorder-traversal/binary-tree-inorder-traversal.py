# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        listinorder = []
        def inorder(root):
            if root==None:
                pass
            else:    
                if root.left:
                    inorder(root.left) 
                listinorder.append(root.val)
                if root.right:
                    inorder(root.right) 
        inorder(root)        
        return listinorder