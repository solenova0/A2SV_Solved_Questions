t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    currMax = a[0]
    summ = 0
    for i in range(1, n):
        if (currMax > 0 and a[i] > 0) or( currMax < 0 and a[i] < 0):
            currMax = max(currMax,a[i])

        else:
            summ += currMax
            currMax = a[i] 
    summ += currMax
    print(summ)