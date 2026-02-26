class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            total = l**2 + r**2
            if total == c:                            
                return True                            

            elif total < c:
                l += 1
            else:
                r -= 1
        return False