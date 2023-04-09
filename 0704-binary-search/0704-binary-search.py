class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums:
            start = 0
            end = len(nums)-1
            while start<=end:
                mid_index = int((start+end)/2)

                if nums[mid_index]==target:
                    return  mid_index
                elif nums[mid_index]>target:
                    end = mid_index-1
                else:
                    start = mid_index+1
            return -1

        else:
            return -1
            