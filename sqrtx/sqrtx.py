class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x==1 or x==0:
            return x
        
        i=2
        n = x/i
        while(n*n>x):
            i+=1
            n=n/i
            
        while(n*n<=x):
            n+=1
        return n-1
        