from collections import Counter
n = int(input())
s = input()
freq = Counter(s)
zeros = freq['r']  
ones = freq['n']
print(*([1]*ones + [0]*zeros))