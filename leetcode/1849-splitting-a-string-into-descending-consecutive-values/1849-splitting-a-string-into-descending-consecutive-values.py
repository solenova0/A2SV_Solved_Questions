class Solution:
    def splitString(self, s: str) -> bool:
        curr = []
    
        def backtrack(index):
            if index >= len(s):
                for i in range(1, len(curr)):
                    if curr[i - 1] - curr[i] != 1:
                        return False
                return len(curr) >= 2
        
            for i in range(index, len(s)):
                val = int(s[index:i+1])
                curr.append(val)
                if backtrack(i + 1):
                    return True
                curr.pop()
            return False  
        return backtrack(0)
