class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = 0
        left = sum(nums)
        for n,i in enumerate(nums):
            left -=i
            if right==left:
                return n
            right+=i
        return -1
         
            
            
    