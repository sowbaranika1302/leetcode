class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapst,mapts = {},{}
        for a,b in zip(s,t):
            if a in mapst and mapst[a]!=b or b in mapts and mapts[b]!=a:
                return False
            mapst[a]=b
            mapts[b]=a
        return True
                
        
       