class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        curr = 0
        freq = {}  
        for v in nums:
            curr += v
            if curr == goal:
                count += 1

            if curr - goal in freq:
                count += freq[curr - goal]
            freq[curr] = freq.get(curr, 0) + 1

        return count