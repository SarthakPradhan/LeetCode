# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        path_arr=[]
        j=0
        def path(root,arr):

            if not root: return

            a=arr+[root.val]

            if not root.left and not root.right:
                path_arr.append(a)
            
            path(root.left,a)
            path(root.right,a)
            
        path(root,[])    
        
        sum_all=0
        print(path_arr)
        for a in path_arr:
            for i in range(len(a)):
                sum_all+=a[len(a)-1-i]*(2**i)
            
        return sum_all
        