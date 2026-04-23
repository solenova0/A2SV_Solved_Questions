class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for v in stones:
            if v in jewels:
                ans += 1
        return ans

        # freq ={v : 0 for v in jewels}
        # for v in stones:
        #     if v in freq:
        #         freq[v] = freq.get(v,0) + 1
        # ans = sum(v for v in freq.values())
        # return ans    
        
