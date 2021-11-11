class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        common_str=""
                
        for i in range (len(strs[0])): 
            comp_str = strs[0][i]
            for j in range(1,len(strs)):
                if (i>=len(strs[j]) or strs[j][i]!=comp_str):
                    return common_str
            common_str+=comp_str
        return common_str
            
                    
            
           
            
        
                    
            
            