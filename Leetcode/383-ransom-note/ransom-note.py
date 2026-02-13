from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      
        # r_counter = Counter(ransomNote)
        # m_counter = Counter(magazine)
        # for c in ransomNote:
        #     if m_counter[c] < r_counter[c]:
        #         return False
        # return True
      
        count = [0] * 26
        for ch in magazine:
            count[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            if count[idx] == 0:
                return False
            count[idx] -= 1

        return True
