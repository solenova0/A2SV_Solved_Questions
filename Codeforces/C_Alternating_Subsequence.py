t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    currMax = a[0]
    summ = 0
    for i in range(1, n):
        if currMax * a[i] < 0:
            summ += currMax
            currMax = a[i]
        else:
             currMax = max(currMax,a[i])    
    summ += currMax
    print(summ)