class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for v in s:
            if v == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(v)
        return "".join(stack)
        