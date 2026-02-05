class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
    
        for v in words:
            temp = list(chars)
            valid = True
            
            for c in v:
                if c in temp:
                    temp.remove(c)
                else:
                    valid = False
                    break
            
            if valid:
                total += len(v)
        
        return total