class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort() 

        def canPlace(dist):
            count = 1
            prev = position[0]

            for i in range(1, len(position)):
                if position[i] - prev >= dist:
                    count += 1
                    prev = position[i]
                if count >= m:
                    return True
            return False

        low, high = 1, position[-1] - position[0]

        while low < high:
            mid = (low + high + 1 ) // 2
            if canPlace(mid):
                low = mid
            else:
                high = mid - 1

        return high

            