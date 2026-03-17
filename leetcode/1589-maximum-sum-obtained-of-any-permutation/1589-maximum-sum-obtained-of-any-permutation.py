class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        d = [0] * n
        for s, e in requests:
            d[s] += 1
            if e < n - 1: d[e + 1] -= 1

        ans = 0
        for delta, num in zip(sorted(list(accumulate(d))), sorted(nums)):
            ans += delta * num
        return ans % (10 ** 9 + 7)