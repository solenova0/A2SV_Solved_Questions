class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        k = skill[0] + skill[-1]
        left = 0
        right = len(skill) - 1
        chem = 0
        while left < right:
            if skill[right] + skill[left] != k:
                return -1
            chem += skill[right] * skill[left]
            left += 1
            right -= 1
        return chem
            