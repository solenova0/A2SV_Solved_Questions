class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        a = s+s
        if goal in a:
            return True
        else:
            return False
        