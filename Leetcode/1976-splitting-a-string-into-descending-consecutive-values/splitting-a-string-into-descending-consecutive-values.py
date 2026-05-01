class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def backtrack(idx, prev, count):
            if idx == n:
                return count >= 2

            num = 0
            for i in range(idx, n):
                num = num * 10 + int(s[i])  

                if prev is None:
                    if backtrack(i + 1, num, count + 1):
                        return True
                else:
                    if num >= prev:
                        break
                    if prev - num == 1:
                        if backtrack(i + 1, num, count + 1):
                            return True

            return False
        return backtrack(0, None, 0)