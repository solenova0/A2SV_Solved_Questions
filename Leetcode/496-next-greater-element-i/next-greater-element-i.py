class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = defaultdict(lambda:-1)
        stack = []
        
        for v in nums2:
            while stack and v > stack[-1]:
                val = stack.pop()
                freq[val] = v
            stack.append(v)

        ans = []
        for i in nums1:
            ans.append(freq[i])
        return ans