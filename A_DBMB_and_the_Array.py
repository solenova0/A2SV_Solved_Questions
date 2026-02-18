t = int(input())
for _ in range(t):
    n , s ,x = map(int, input().split())
    a = list(map(int, input().split()))
    summ = sum(a)
    if (s - summ) % x == 0 and summ <= s:
        print("YES")
    else:
        print("NO")