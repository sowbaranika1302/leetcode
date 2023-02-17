class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        sqrt5 = sqrt(5)
        return int((pow(1 + sqrt5, n) - pow(1 - sqrt5, n)) / pow(2, n) / sqrt5)