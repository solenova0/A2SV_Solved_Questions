class Solution:
    def checkEqual(self, a, b) -> bool:
        a.sort()
        b.sort()
        i = 0
        if len(b) != len(a):
            return False
        else:
            while i < len(b):
                if b[i] != a[i]:
                    return False
                i += 1
        return True
        