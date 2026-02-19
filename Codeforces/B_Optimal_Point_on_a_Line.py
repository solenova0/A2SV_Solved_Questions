n = int(input())
x = list(map(int, input().split()))
x.sort()
if n % 2 == 1:
    print(x[n // 2])
else:       
    print(x[n // 2 - 1])
