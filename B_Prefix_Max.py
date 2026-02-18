t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxx = max(a)
    print(n * maxx)
