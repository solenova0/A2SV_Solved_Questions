def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a = list(set(a))
    a.sort()

    v = 0
    ans = 0

    for i in range(len(a)):
        while a[i] - a[v] >= n:
            v += 1
        ans = max(ans, i - v + 1)
    print(ans)
    
t = int(input())
for _ in range(t):
    solve()