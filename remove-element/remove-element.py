class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        incr = 0
        l = len(nums)
        for i in range(l):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
                
                
        return index
                
            
        