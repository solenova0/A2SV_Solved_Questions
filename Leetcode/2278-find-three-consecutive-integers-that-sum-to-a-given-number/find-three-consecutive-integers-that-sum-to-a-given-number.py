class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        if num % 3 == 0:
            ans.append(num//3 -1)
            ans.append(num//3)
            ans.append(num//3 + 1)
        return ans