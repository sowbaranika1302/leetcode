class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        for i in Counter(s).values():
            count+= i//2*2
            if i%2==1 and count%2 ==0:
                count+=1
        return count

