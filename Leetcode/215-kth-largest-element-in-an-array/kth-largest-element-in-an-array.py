class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [v for v in nums if v > pivot]
        mid = [v for v in nums if v == pivot]
        right = [v for v in nums if v < pivot]

        l = len(left)
        r = len(right)
        m = len(mid)
        if k <= l:
            return self.findKthLargest(left, k)
        elif k > l + m:
            return self.findKthLargest(right, k - m - l)
        else:
            return mid[0]
