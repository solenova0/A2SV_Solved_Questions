class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        count = 0
        for x in freq:
            count += ceil(float(freq[x]) / (x + 1)) * (x + 1)
        return int(count)