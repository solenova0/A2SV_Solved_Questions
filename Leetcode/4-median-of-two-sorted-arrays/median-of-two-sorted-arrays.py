class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def kth(k):
            if len(nums1) > len(nums2):
                return kth_from(nums2, nums1, k)
            return kth_from(nums1, nums2, k)

        def kth_from(A, B, k):
            l, r = 0, len(A)
            
            while l < r:
                mid = (l + r) // 2
                count = mid + bisect.bisect_left(B, A[mid])
                
                if count < k:
                    l = mid + 1
                else:
                    r = mid
            
            candi = []
            
            if l < len(A):
                candi.append(A[l])
            
            idx = k - l
            if 0 <= idx < len(B):
                candi.append(B[idx])
            
            return min(candi)

        total = len(nums1) + len(nums2)
        
        if total % 2 == 1:
            return kth(total // 2)
        else:
            return (kth(total // 2 - 1) + kth(total // 2)) / 2

        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1

        # total = len(nums1) + len(nums2)
        # half = total // 2

        # l = 0
        # r = len(nums1)

        # while True:
        #     i = (l + r) // 2 
        #     j = half - i              

        #     l_1 = nums1[i - 1] if i > 0 else float("-inf")
        #     r_1 = nums1[i] if i < len(nums1) else float("inf")

        #     l_2 = nums2[j - 1] if j > 0 else float("-inf")
        #     r_2 = nums2[j] if j < len(nums2) else float("inf")

        #     # correct partition
        #     if l_1 <= r_2 and l_2 <= r_1:
        #         if total % 2:
        #             return min(r_1, r_2)
        #         else:
        #             return (max(l_1, l_2) + min(r_1, r_2)) / 2

        #     elif l_1 > r_2:
        #         r = i - 1
        #     else:
        #         l = i + 1