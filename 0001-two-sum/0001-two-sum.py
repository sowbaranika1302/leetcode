class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i,n in enumerate(nums):
            if target-n in new_dict:
                return [i,new_dict[target-n]]
            new_dict[n] = i
                
        
           
        