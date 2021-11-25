class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for a in nums[1:]:
            if a>=sums[-1]+a:
                sums.append(a)
            else:
                sums.append(sums[-1]+a)
                
        return max(sums)