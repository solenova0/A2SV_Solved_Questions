from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.count = defaultdict(int)   
        self.freq = defaultdict(int)    

    def add(self, number: int) -> None:
        old = self.count[number]
        if old > 0:
            self.freq[old] -= 1

        self.count[number] += 1
        new = self.count[number]
        self.freq[new] += 1

    def deleteOne(self, number: int) -> None:
        old = self.count[number]
        if old == 0:
            return

        self.freq[old] -= 1
        self.count[number] -= 1
        new = self.count[number]

        if new > 0:
            self.freq[new] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
