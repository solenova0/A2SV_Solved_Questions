t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    values = []
    freq = []
    for x in arr:
        if not values or values[-1] != x:
            values.append(x)
            freq.append(1)
        else:
            freq[-1] += 1
    l = 0
    total = 0
    ans = 0
    
    for r in range(len(values)):
        if r > 0 and values[r] != values[r-1] + 1:
            l = r
            total = 0
        total += freq[r]
        while r - l + 1 > k:
            total -= freq[l]
            l += 1
        ans = max(ans, total)
    print(ans)