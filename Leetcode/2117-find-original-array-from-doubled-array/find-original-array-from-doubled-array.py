class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []

        changed.sort()
        count = Counter(changed)
        original = []

        for x in changed:
            if count[x] == 0:
                continue
            
            if count[2 * x] == 0:
                return []

            original.append(x)
            count[x] -= 1
            count[2 * x] -= 1

        return original

# Time: O(n log n) (sorting)
# Space: O(n) (counter + result)