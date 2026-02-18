class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(n):
            maxm = i
            for j in range(i + 1 , n):
                if heights[j] > heights[maxm]:
                    maxm = j
            heights[i] ,heights[maxm] = heights[maxm] , heights[i]
            names[i] ,names[maxm] = names[maxm] , names[i]
        return names