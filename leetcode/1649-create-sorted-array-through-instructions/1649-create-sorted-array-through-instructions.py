class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        arr = []
        cost = 0

        for x in instructions:
            left = bisect.bisect_left(arr, x)
            right = len(arr) - bisect.bisect_right(arr, x)

            cost += min(left, right)
            bisect.insort(arr, x)

        return cost % (10**9 + 7)