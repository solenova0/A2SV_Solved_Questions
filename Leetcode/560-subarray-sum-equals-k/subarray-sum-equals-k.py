from collections import defaultdict
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1   
        
        summ = 0
        ans = 0
        
        for num in nums:
            summ += num
            if summ - k in freq:
                ans += freq[summ - k]
            freq[summ] += 1
        
        return ans