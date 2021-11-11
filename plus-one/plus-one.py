class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1]!=9:
            digits[-1]+=1
        else:
            carry = 1
            i=-1
            while(carry!=0):
                if digits[i]!=9:
                    digits[i]+=1
                    carry=0
                elif (i+len(digits) == 0):
                    digits[i]=0
                    digits.insert(0,1)
                    carry=0
                    
                else:
                    digits[i]=0
                    
                    
                i-=1
                
        return digits
                    
                    
        