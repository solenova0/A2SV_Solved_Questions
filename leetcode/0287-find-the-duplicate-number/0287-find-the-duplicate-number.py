class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Not Follow Constraint : Do not Update
        i = 0
        while i < len(nums):
            idx = nums[i] - 1
            
            if nums[i] != nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                if i != idx:
                    return nums[i] 
                i += 1

        # slow = nums[0]
        # fast = nums[0]
        
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break
        
        # slow2 = nums[0]
        # while slow != slow2:
        #     slow = nums[slow]
        #     slow2 = nums[slow2]

        # return slow