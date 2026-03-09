class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        freq = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in freq:
                if not stack:      
                    return False  
                top = stack.pop()
                if top != freq[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack