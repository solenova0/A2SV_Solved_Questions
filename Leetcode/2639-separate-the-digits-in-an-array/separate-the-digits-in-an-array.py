class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for v in nums:
            v = str(v)
            i = 0
            while i < len(v):
                ans.append(int(v[i]))
                i += 1
                    
        return ans