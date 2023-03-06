class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss = []
        j=0
        for i in range(1,len(arr)+k):
            if arr[j]!=i:
                miss.append(i)
                print(miss)
                if (len(miss))==k:
                    
                    return miss[k-1]
            else:
                j+=1
                if(j==len(arr)):
                     return arr[::-1][0]+k-len(miss)
       
         
                
                
            
            
        