

def min_time(n, k):
    if k > n:
        return -1
    if k == n:
        return 0
    if k == 0:
        return -1
    left = n // 2
    right = n - left
    t1 = min_time(left, k)
    t2 = min_time(right, k)
    if t1 == -1 and t2 == -1:
        return -1
    elif t1 == -1:
        return t2 + 1
    elif t2 == -1:
        return t1 + 1
    else:
        return min(t1, t2) + 1

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(min_time(n, k))
