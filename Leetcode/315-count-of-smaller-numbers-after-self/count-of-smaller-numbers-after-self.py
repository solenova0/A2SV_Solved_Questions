class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        enum = list(enumerate(nums))  # (index, value)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            merged = []
            j = 0
            
            for i in range(len(left)):
                while j < len(right) and left[i][1] > right[j][1]:
                    j += 1
                res[left[i][0]] += j
            
            return sorted(left + right, key=lambda x: x[1])

        merge_sort(enum)
        return res
