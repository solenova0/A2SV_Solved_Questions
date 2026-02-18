class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        freq = Counter(nums)
        
        dom, total = max(freq.items(), key=lambda x: x[1])
        
        leftCount = 0
        for i in range(n - 1):
            if nums[i] == dom:
                leftCount += 1
            
            if leftCount * 2 > (i + 1) and (total - leftCount) * 2 > (n - i - 1):
                return i
        return -1
