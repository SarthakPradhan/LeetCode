class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        i=0
        while  i<len(numbers):
            if (target-numbers[i]) in dict:
                return [dict[target-numbers[i]]+1,i+1]
            dict[numbers[i]] = i
            i+=1