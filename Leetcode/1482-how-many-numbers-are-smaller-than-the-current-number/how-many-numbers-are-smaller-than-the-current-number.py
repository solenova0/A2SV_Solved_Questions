class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def count_smaller(nums):
            if not nums:
                return []
        n= max(nums)
        count = [0] * (n + 1)

        for num in nums:
            count[num] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        res = []
        for num in nums:
            if num  == 0:
                res.append(0)
            else:
                res.append(count[num - 1])

        return res
