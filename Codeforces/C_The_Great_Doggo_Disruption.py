from collections import Counter
n = int(input())
s = input()
freq = Counter(s)
if len(freq) > 1 and all(v == 1 for v in freq.values()):
    print("No")
else:
    print("Yes")