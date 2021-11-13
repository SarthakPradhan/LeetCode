class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        h = len(haystack)
        n = len(needle)
        
        if not needle: return 0
        
        if h<n: return -1
        
        
        index = -1
        
        """
        
        for i in range(h-n+1):
            
            if haystack[i]== needle[0]:
                index = i
                for j in range(len(needle)):
                    if  haystack[i+j]!=needle[j]:
                        index = -1
                        break
                    
                if index != -1 :
                    return index
        """
        
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
                
                        
        return index
            
                
        