class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for v in str(nums[i]):
                ans.append(int(v))


        return ans