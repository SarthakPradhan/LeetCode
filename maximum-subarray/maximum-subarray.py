class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums_array=[]
        
        sum_l=nums[0]
        max_l=sum_l
        start_i=0
        end_i=0
        max_index = 0
        
        l =  len(nums)
        if l == 1:
            return nums[0]
        
        
        else:
            sums_array.append(nums[0])
            for i in range(1,l):
            
                if sums_array[-1] + nums[i]<=nums[i]:
                    sums_array.append(nums[i])
                    
                else:
                    sums_array.append(sums_array[i-1] + nums[i])
                 
                
        return max(sums_array)