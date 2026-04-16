def myfun(arr, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    myfun(arr, l, mid)
    myfun(arr, mid + 1, r)

    size = r - l + 1
    wins = [0] * size
    temp = mid + 1
    for i in range(l, mid + 1):
        while temp <= r and arr[temp][1] < arr[i][1]:
            temp += 1
        wins[i - l] = temp - (mid + 1)

    temp = l
    for i in range(mid + 1, r + 1):
        while temp <= mid and arr[temp][1] < arr[i][1]:
            temp += 1
        wins[i - l] = temp - l

    merged = []
    i, j = l, mid + 1

    while i <= mid or j <= r:
        if j > r or (i <= mid and arr[i][1] + wins[i - l] < arr[j][1] + wins[j - l]):
            merged.append((arr[i][0], arr[i][1] + wins[i - l]))
            i += 1
        else:
            merged.append((arr[j][0], arr[j][1] + wins[j - l]))
            j += 1

    arr[l:r + 1] = merged

t = int(input())
for _ in range(t):
    n = int(input())
    values = list(map(int, input().split()))
    arr = [(i, v) for i, v in enumerate(values)]
    myfun(arr, 0, (2 ** n) - 1)
    arr.sort()  
    print(*[v for _, v in arr])