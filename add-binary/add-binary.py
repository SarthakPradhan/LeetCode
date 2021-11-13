class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        dec2bin = {0:[0,0],1:[0,1],2:[1,0],3:[1,1]}
        
        carry = 0
        
        out = ''
        
        m = len(a)
        n = len(b)
        
        l = max(m,n)
        
        for i in (range(1,l+1)):
            if m - i < 0 :
                l1 = 0
                l2 = int(b[-i])
                
                
                
            elif n - i < 0:

                l1 = int(a[-i])
                l2 = 0
                
            else:
                l1 = int(a[-i])
                l2 = int(b[-i])
                
            sum = carry + l1 + l2
            carry = (dec2bin[sum])[0]
            out = str((dec2bin[sum])[1]) + out
        if carry == 1:
            out = str(carry)+out
        return out