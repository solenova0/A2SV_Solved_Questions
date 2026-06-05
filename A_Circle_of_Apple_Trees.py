from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int , input().split()))
    freq = Counter(a)
    count = 0
    for v in freq.values():
        if  v > 1:
            count += v - 1
    print(n - count)
