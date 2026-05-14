def check(a, mid):
    temp = a[:]
    if mid > 0:
        temp[:mid] = sorted(temp[:mid])
        temp[-mid:] = sorted(temp[-mid:])
    return temp == sorted(a)

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if check(a, mid):
            high = mid - 1
        else:
            low = mid + 1
    print(low)

for _ in range(int(input())):
    solve()