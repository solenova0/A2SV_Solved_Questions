import bisect
bisect 
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(q):
        k, x = map(int, input().split())
        temp = sorted(arr[:k])  
        ans = bisect.bisect_left(temp, x)
        print(ans)