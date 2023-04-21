class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i,n in enumerate(nums):
            if target - n in new_dict:
                return [new_dict[target-n],i]
            new_dict[n] =i
        
           
        