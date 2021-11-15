class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i] = 1
                
        val_list = list(count.values())
        key_list = list(count.keys())
 
        return key_list[val_list.index(1)]
        