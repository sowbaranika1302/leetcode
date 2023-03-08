class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 1
        i,j = 0,1
        while j in range(len(nums)):
            if nums[i]==nums[j]:
                
                nums.remove(nums[j])
            else:
                i = j
                j+=1
                unique_count+=1    
        return unique_count
        