
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        freq = {}
        freq[0]=-1
        summ=0
        for i,j in enumerate(nums):
            summ+=j
            if summ%k in freq.keys():
                if i-freq[summ%k]>=2:
                    return True
                else:
                    continue
            freq[summ%k]=i
        return False
            
