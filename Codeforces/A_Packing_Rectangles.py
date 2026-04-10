w, h, n = map(int, input().split())
def can(x):
    return (x // w) * (x // h) >= n
l, r = 1, 10**18

while l < r:
    mid = (l + r) // 2
    if can(mid):
        r = mid
    else:
        l = mid + 1

print(l)