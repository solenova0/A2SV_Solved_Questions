class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        res = []
        for v in nums1Set:
            if v in nums2Set:
                res.append(v)
        return res
