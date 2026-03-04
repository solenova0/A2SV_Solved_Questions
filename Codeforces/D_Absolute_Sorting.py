t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, (x for x in input().split())))

    if arr == sorted(arr):
        print(0)
        continue

    if len(set(arr)) == 2:
        ma = max(arr)
        mi = min(arr)

        if (ma - mi) % 2 == 0:
            print(mi + ((ma - mi) // 2))
            continue


    x = 81409090 - 29613295  
    for i in range(n):
        arr[i] = abs(arr[i] - x)
    print(arr)
    if arr == sorted(arr):
        print(x)
    else:
        print(-1)    
