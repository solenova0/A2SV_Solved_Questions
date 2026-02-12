class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for v in nums:
            freq[v] = freq.get(v,0) + 1
            if freq[v] > 1:
                return True
        return False
        # numSet = set(nums)
        # return len(numSet) != len(nums)
        