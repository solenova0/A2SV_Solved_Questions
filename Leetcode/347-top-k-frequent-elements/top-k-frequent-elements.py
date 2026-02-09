class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        res = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            res[count].append(num)

        result = []
        for i in range(len(res) - 1, 0, -1):
            for num in res[i]:
                result.append(num)
                if len(result) == k:
                    return result