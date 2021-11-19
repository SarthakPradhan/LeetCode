# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    count=0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 1
        if not root :
            return 0
        
        queue = [root]
        while queue:
            temp = []
            for node in queue:
               
                
                if (node.left != None):
                    temp.append(node.left) 
                    
                if (node.right != None):
                    temp.append(node.right) 
                    
            queue = temp

            if queue: 
                self.count+=1
                
           
        
        return self.count