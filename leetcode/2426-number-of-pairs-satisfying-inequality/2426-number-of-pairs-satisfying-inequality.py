class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [a - b for a, b in zip(nums1, nums2)]
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums, 0
            
            mid = len(nums) // 2
            l, count_l = merge_sort(nums[:mid])
            r, count_r = merge_sort(nums[mid:])
            
            count = count_l + count_r

            #Count Step
            j = 0
            for i in range(len(l)):
                while j < len(r) and l[i] > r[j] + diff:
                    j += 1
                count += len(r) - j
            
            #merge
            merged = []
            i = j = 0
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    merged.append(l[i])
                    i += 1
                else:
                    merged.append(r[j])
                    j += 1
            
            merged.extend(l[i:])
            merged.extend(r[j:])
            
            return merged, count
        
        return merge_sort(arr)[1]