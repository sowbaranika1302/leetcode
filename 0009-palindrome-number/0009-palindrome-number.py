class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        pal = 0
        while x and x>0:
            num = x%10
            pal = pal*10 +num
            x = x//10
        if pal == a:
            return True
        return False