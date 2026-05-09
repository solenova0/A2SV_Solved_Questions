class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count('L')
        v = moves.count('_')
        r = moves.count('R')
        return abs(l - r) + v
    