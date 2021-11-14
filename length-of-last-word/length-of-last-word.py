class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        
        flag = False
        for i in range(len(s)):
            if s[i] == " " :
                flag = True
                    
            elif flag == True:
                length = 1
                flag = False
            
            else:
                length += 1
        return length
        