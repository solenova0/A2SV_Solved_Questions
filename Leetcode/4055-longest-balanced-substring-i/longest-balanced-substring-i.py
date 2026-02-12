class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26
            mx = 0 
            v = 0  
            for j in range(i, n):
                c = ord(s[j]) - ord('a')
                if freq[c] == 0:
                    v += 1
                    
                freq[c] += 1
                mx = max(mx, freq[c])
                if mx * v == (j - i + 1):
                    ans = max(ans, j - i + 1)

        return ans
