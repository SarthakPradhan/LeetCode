class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid = True
        dict_brackets = {')':'(', '}':'{',']':'['}
        stack = []
        for c in s:
            if c in dict_brackets:
                if not stack or stack[-1] !=dict_brackets[c]:                 
                    valid = False
                else:
                    stack.pop()
                    
            else:
                stack.append(c)
        if  stack:
            valid = False
                
        return(valid)
                    
        
        
        
            
        