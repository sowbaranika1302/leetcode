class Solution:
    
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n not in mem:
            if(n==1):
                return True
            mem.add(n)
            n = self.sumHappy(n)
        return False
    
    def sumHappy(self, n: int):
        
        count = 0
        while n:
            m = n%10
            count+= m*m
            n = n//10
        return (count)
    
    
        