class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c,0) + 1
        for i, key in enumerate(s):
            if freq[key] == 1:
                return i

        return -1