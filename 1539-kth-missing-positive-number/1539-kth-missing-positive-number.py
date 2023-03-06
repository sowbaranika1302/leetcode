class Solution:
    def findKthPositive(self, A: List[int], k: int) -> int:
        l,r = 0,len(A)
        while l<r:
            m = (l+r) //2
            if A[m]-(m+1)<k:
                l = m+1
            else:
                r= m
        return l+k
                
                
            
            
        