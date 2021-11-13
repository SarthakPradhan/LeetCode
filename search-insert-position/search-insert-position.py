class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start_ind = 0
        end_ind = len(nums)
        
        if target<=nums[start_ind]: 
            return 0
        elif target>nums[end_ind-1]:
            return end_ind
        
        while end_ind-start_ind >1:
            
            mid_ind = (start_ind+end_ind)/2
            
            if target == nums[mid_ind]:
                return mid_ind
        
            elif target>nums[mid_ind]:
                start_ind = mid_ind
                
            else:
                end_ind = mid_ind
                
        return end_ind
            
        