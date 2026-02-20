class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {c: 0 for c in order}
        for c in s:
            if c in freq:
                freq[c] += 1
    
        ans = ''
        for c in order:
            ans += c * freq[c]
    
        for c in s:
            if c not in order:
                ans += c
        print(ans)
        return ans



        