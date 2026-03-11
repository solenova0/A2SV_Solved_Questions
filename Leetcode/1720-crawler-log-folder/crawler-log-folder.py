class Solution:
    def minOperations(self, logs: List[str]) -> int:
        d = 0
        for log in logs:
            if log == "../":
                d -= 1 if d > 0 else 0
            elif log == "./":
                d += 0
            else:
                d += 1
        return d