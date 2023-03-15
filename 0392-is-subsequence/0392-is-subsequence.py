class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if not s:
            return i==len(s)
            
        for j in t:  
            if s[i]==j:
                i+=1
                if i ==len(s):
                    return True
        return False
    