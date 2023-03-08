class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 1,1
        while j in range(len(nums)):
            if nums[j]!=nums[j-1]:
                nums[i] = nums[j]
                i+=1
            j+=1  
        return i
        