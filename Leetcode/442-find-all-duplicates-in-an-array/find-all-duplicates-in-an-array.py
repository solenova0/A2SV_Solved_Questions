class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for v in nums:
            freq[v] = freq.get(v,0) + 1
            if freq[v] == 2:
                res.append(v)
        return res