class Solution:
    def findValidPair(self, s: str) -> str:
        freq = {}
        for v in s:
            freq[v] = freq.get(v, 0) + 1

        for i in range(len(s) - 1):
            a = int(s[i])
            b = int(s[i + 1])

            if a != b:
                if freq[s[i]] == a and freq[s[i + 1]] == b:
                    return s[i] + s[i + 1]

        return ""

            
