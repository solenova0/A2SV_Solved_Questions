class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # for c in t:
        #     if t.count(c) > s.count(c):
        #         return(c)
        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) + 1

        for c in s:
            freq[c] -= 1
            if freq[c] == 0:
                del freq[c]

        return list(freq.keys())[0]