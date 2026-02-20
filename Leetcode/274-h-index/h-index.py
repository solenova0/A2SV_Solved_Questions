class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # n = len(citations)
        # arr = [0 for _ in range(n + 1)]

        # for i,v in enumerate(citations):
        #     if v > n :
        #         arr[n] += 1
        #     else:
        #         arr[v] += 1
        
        # total = 0
        # for i in range(n, -1, -1):
        #     total += arr[i]
        #     if total >= i:
        #         return i
 
        n = len(citations)
        citations.sort()

        for i, citation in enumerate(citations):
            if citation >= n - i:
                return n - i

        return 0