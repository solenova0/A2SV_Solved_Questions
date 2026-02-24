class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str: 
        def is_subsequence(word, s):
            i = 0
            j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            return i == len(word)
        
        best = ""
        for word in dictionary:
            if is_subsequence(word, s):
                if len(word) > len(best):
                    best = word
                
                elif len(word) == len(best) and word < best:
                    best = word
        
        return best