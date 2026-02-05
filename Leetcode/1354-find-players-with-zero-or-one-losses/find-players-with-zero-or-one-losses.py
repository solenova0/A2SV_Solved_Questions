class Solution:
    def findWinners(self, matches):
        freq = {}
        ans = []
        res = []
        players = set()
        for i in range(len(matches)):
            winner = matches[i][0]
            loser = matches[i][1]
            players.add(winner)
            players.add(loser)
            freq[loser] = freq.get(loser, 0) + 1

        for p in players:
            if freq.get(p, 0) == 0:
                ans.append(p)
            elif freq[p] == 1:
                res.append(p)

        return [sorted(ans), sorted(res)]
