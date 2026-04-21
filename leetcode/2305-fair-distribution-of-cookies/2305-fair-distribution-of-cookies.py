class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        children = [0] * k
        self.ans = float('inf')

        def backtrack(i):
            if i == n:
                self.ans = min(self.ans, max(children))
                return
            if max(children) >= self.ans:
                return

            for j in range(k):
                children[j] += cookies[i]

                backtrack(i + 1)
                children[j] -= cookies[i]
                if children[j] == 0:
                    break

        backtrack(0)
        return self.ans
    
        