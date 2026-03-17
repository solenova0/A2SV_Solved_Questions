class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
                seen = {}
                res = 0
                l = 0

                for r in range(len(nums)):
                    if nums[r] not in seen:
                        seen[nums[r]] = 0
                        k -= 1
                    seen[nums[r]] += 1

                    while k < 0:
                        seen[nums[l]] -= 1
                        if seen[nums[l]] == 0:
                            del seen[nums[l]]
                            k += 1
                        l += 1

                    res += r - l + 1

                return res

        return atMost(k) - atMost(k - 1)