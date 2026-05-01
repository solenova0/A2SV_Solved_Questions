class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        bucket = [[] for _ in range(len(nums))]

        mi = min(nums)
        ma = max(nums)
        if ma == mi:
            return 0

        for i in nums:
            idx = int((i - mi) / (ma-mi) * (len(nums)-1)) 
            bucket[idx].append(i)

        ans = []
        for i in bucket:
            if i:
                i.sort()
                ans.extend(i)
        res = 0
        for i in range(1, len(ans)):
            res = max(res, ans[i]-ans[i-1])
        return res
