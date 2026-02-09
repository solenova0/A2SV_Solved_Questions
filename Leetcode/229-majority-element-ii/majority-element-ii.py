class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        n = len(nums)// 3
        lists =[]
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for key in freq:
            if freq[key] > n:
                lists.append(key)
        return lists
        