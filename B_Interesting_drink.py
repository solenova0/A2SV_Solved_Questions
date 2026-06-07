from bisect import bisect_right
n = int(input())
a = list(map(int, input().split()))
a.sort()

q = int(input())
for _ in range(q):
    x = int(input())
    print(bisect_right(a, x))