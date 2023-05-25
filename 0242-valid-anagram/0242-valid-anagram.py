class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s)!=len(t):
            return False
        for i in s:
            dic[i] = dic.get(i,0)+1
        for i in t:
            if i not in dic or dic.get(i)==0:
                return False
            dic[i] = dic.get(i)-1
        return True
        