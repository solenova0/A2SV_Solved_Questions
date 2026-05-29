class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')

        for v in nums:
            digit_sum = 0

            for ch in str(v):
                digit_sum += int(ch)

            ans = min(ans, digit_sum)

        return ans
