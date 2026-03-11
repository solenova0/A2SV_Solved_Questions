class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        shift = [0] * (n + 1)
        for v in shifts:
            start, end, dirc = v
            shift[start] += (1 if dirc == 1 else -1)
            if end + 1 < n:
                shift[end + 1] -= (1 if dirc == 1 else -1)

        curr = 0
        ans = list(s)
        for i in range(n):
            curr += shift[i]
            n = (curr % 26 + 26) % 26
            ans[i] = chr((ord(ans[i]) - ord('a') + n) % 26 + ord('a'))

        return ''.join(ans)