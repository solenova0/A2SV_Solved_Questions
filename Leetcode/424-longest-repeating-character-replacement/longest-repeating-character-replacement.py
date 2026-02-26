class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        
        l = 0
        v = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            v = max(v, freq[s[r]])

            if (r - l + 1) - v > k:
                freq[s[l]] -= 1
                l += 1

        return (r - l + 1)
A