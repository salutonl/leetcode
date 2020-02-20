class Solution:
    def isHappy(self, n):
        loop = set()
        while n != 1:
            loop.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
            if n in loop:
                return False
        return True
