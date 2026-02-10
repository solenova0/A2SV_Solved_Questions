class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n  not in seen:
            seen.add(n)
            summ = 0

            while n > 0:
                summ += (n % 10)** 2
                n //=  10
            n = summ
            if summ == 1:
                return True
        return False 


        