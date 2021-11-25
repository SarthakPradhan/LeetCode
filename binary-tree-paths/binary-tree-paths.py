# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        pathlist = []
        
        def addPath(path_str,root):
            
            if root == None: return
            path_str = path_str+str(root.val)+"->"
            if root.left == None and root.right == None:
                path_str = path_str[:-2]
                pathlist.append(path_str)
                
            if root.left:
                addPath(path_str,root.left)
                
            if root.right:
                addPath(path_str,root.right)
        
        addPath("",root)
        return pathlist