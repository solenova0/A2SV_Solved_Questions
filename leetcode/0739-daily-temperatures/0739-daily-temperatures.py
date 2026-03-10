class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i, value in enumerate(temperatures):
            while stack and stack[-1][1] < value:
                idx , val = stack.pop()
                ans[idx] = i - idx
            stack.append([i , value])
        return ans