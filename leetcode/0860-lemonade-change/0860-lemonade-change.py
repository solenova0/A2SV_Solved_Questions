class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a = 0
        b = 0
        if bills[0] != 5 or bills[1] == 20:
            return False
        for v in bills:
            if v == 5:
                a += 1
            elif v == 10 and a > 0:
                a -= 1
                b += 1
            elif v == 20 and 15 <= a * 5 + 10 * b:
                if b > 0 and a > 0:
                    b -= 1
                    a -= 1
                elif a >= 3:
                    a -= 3
                else:
                    return False
            else:
                return False
        return True






        