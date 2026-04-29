class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):

                a = num[:i]
                b = num[i:j]
                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                    continue

                if self.check(a, b, num[j:]):
                    return True

        return False
    def check(self, a, b, rest):
        while rest:
            c = str(int(a) + int(b))

            if not rest.startswith(c):
                return False

            rest = rest[len(c):]
            a, b = b, c

        return True