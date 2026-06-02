class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration,
    ):
        n = len(landStartTime)
        m = len(waterStartTime)

        INF = 10**18
        res = INF

        for i in range(n):
            land_end = landStartTime[i] + landDuration[i]

            for j in range(m):
                start = max(land_end, waterStartTime[j])
                res = min(res, start + waterDuration[j])

        for j in range(m):
            water_end = waterStartTime[j] + waterDuration[j]

            for i in range(n):
                start = max(water_end, landStartTime[i])
                res = min(res, start + landDuration[i])

        return res