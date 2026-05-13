class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        temp = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            temp[2] += 2
            temp[a + 1] -= 1
            temp[a + b] -= 1
            temp[a + b + 1] += 1
            temp[b + limit + 1] += 1

        moves = n
        curr = 0

        for c in range(2, 2 * limit + 1):
            curr += temp[c]
            if curr < moves:
                moves = curr

        return moves