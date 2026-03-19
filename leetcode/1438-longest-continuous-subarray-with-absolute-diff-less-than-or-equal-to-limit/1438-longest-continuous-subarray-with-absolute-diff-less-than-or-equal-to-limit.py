from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        maxx = deque()
        minn = deque()
        left = 0
        ans = 0

        for right in range(len(nums)):
            while maxx and nums[right] > nums[maxx[-1]]:
                maxx.pop()
            maxx.append(right)

            while minn and nums[right] < nums[minn[-1]]:
                minn.pop()
            minn.append(right)

            while nums[maxx[0]] - nums[minn[0]] > limit:
                if maxx[0] == left:
                    maxx.popleft()
                if minn[0] == left:
                    minn.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans