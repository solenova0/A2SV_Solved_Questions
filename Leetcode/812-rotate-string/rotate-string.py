class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # a = s+s
        # if goal in a:
        #     return True
        # else:
        #     return False
        n = len(s)
        for i in range(len(s)):
            s = s[-1] + s[:n - 1]
            if s == goal:
                return True
        return False