t = int(input())
for _ in range(t):
    n , k = map(int,input().split())
    arr  = []
    for i in range(n):
        v =  [int(i) for i in input().split()]
        arr.append(v)
    arr.sort()
    for i in  (arr):
        if i[0] <= k  and   i[2]  > k:
            k =  i[2]
    print(k)

