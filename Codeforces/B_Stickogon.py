from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a) 
    ans = 0
    for count in freq.values():
        ans += count // 3
    
    print(ans)