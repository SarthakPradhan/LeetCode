class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup_check = {}
        for i in nums:
            if i in dup_check:
                return True
            else:
                dup_check[i]=1
            
        return False