class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1, l2 = len(needle), len(haystack)

        if needle in haystack:
            window = haystack[:l1]
            if window == needle:
                return 0

            for i in range(l1, l2):
                window = window[1:] + haystack[i] 
                if window == needle:
                    return i - l1 + 1 

        return -1