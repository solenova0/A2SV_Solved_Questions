class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        v = 0
        for i in range(len(nums)):
            v += nums[i]
            res.append(v)
        return res
