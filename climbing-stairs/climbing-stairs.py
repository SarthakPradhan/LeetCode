class Solution(object):
    def fact(self,m):
        if m == 1 or m == 0:
            return 1
        else: return m*self.fact(m-1)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range (n/2+1):
            count += self.fact(n-i)/(self.fact(i)*self.fact(n-2*i))
        
        return count
        
        
            
            
            