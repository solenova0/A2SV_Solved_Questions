class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(houses)
        m = len(heaters)
        heaters.sort()
        ans = 0
        for v in houses:
            idx = bisect.bisect_left(heaters, v)

            if idx==0:
                nearest = heaters[0] - v
            elif idx==m:
                nearest = v - heaters[-1]
            else:
                nearest = min(heaters[idx]-v, v - heaters[idx-1])
            ans = max(ans, nearest)
        return ans