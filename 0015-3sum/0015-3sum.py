class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,n in enumerate(nums):
            if i>0 and nums[i-1] == n:
                continue
            left = i+1
            right = len(nums)-1
            while(left<right):
                sums = n+nums[left] +nums[right]        
                if sums == 0:
                    res.append([n,nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                elif sums>0:
                    right-=1
                else:
                    left+=1
        return res
                
        
            