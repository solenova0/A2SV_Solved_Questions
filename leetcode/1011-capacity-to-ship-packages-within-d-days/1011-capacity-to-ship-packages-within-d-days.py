class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        ans = sum(weights)

        def check(mid):
            day, curr = 1, mid
            for w in weights:
                if curr - w < 0:
                    day += 1
                    curr = mid
                curr -= w
            return day <= days

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans



