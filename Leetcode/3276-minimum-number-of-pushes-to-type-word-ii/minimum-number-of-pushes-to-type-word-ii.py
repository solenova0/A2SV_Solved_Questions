class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        ans = 0
        for i, (_, cnt) in enumerate(freq):
            ans += (i // 8 + 1) * cnt

        return ans