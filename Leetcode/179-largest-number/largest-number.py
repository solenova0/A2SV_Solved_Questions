class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # for i, n in enumerate(nums):
        #     nums[i] = str(n)

        # def compare(n1, n2):
        #     if n1 + n2 > n2 + n1:
        #         return -1
        #     else:
        #         return 1

        # nums = sorted(nums, key = cmp_to_key(compare))

        # return str(int("".join(nums)))

        nums = [str(n) for n in nums]
        
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        if nums[0] == "0":
            return "0"

        return "".join(nums)