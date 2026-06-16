class Solution:
    def processStr(self, s: str) -> str:
        res = []
        n = len(s)

        for i in range(n):
            c = s[i]

            if c == '*':
                if len(res) != 0:
                    res.pop()
            elif c == '#':
                res.extend(res)
            elif c == '%':
                res.reverse()
            elif 'a' <= c <= 'z':
                res.append(c)

        return ''.join(res)