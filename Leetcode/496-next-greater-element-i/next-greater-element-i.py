class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                freq[prev] = num
            stack.append(num)

        for num in stack:
            freq[num] = -1

        return [freq[num] for num in nums1]