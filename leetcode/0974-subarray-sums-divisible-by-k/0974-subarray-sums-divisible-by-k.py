class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1 
        
        curr_sum = 0
        count = 0
        
        for x in nums:
            curr_sum += x
            r = (curr_sum % k + k) % k
            
            count += freq[r]
            freq[r] += 1
        
        return count