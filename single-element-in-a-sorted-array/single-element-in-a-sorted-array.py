class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1 
        while start != end:
            
            n = (end+start)//2

            if nums[n] == nums[n-1] and n%2 == 0:
                end = n-2
            elif nums[n] == nums[n-1] and n%2 != 0:
                start = n+1
            elif nums[n] == nums[n+1] and n%2 == 0:
                start = n+2
            elif nums[n] == nums[n+1] and n%2 != 0:
                end = n-1
                
            else:
                return nums[n]
            
        return nums[start]