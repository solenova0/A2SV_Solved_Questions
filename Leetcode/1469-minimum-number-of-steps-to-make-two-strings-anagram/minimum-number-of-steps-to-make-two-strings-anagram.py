class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            count[ord(c) - ord('a')] -= 1
        
        # Only positive differences in s count toward steps
        steps = 0
        for x in count:
            if x > 0:
                steps += x
        
        return steps