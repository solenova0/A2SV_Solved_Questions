class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                #choose
                used[i] = True
                path.append(nums[i])
                #explore
                backtrack()
                #un-choose (backtrack)
                path.pop()
                used[i] = False

        backtrack()
        return res