class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for n,i in enumerate(nums):
            right -=i
            if right==left:
                return n
            left+=i
        return -1
         
            
            
    