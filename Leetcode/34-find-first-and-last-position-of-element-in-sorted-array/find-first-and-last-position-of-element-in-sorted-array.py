class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def myFun(isFirst):
            v = - 1
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    v = mid
                    if isFirst:
                        high = mid - 1  
                    else:
                        low = mid + 1   
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return v

        return [myFun(True), myFun(False)]