# import math

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
    
#     arr.sort()
#     g = 0
    
#     for i in range(1, n):
#         g = math.gcd(g, arr[i] - arr[0])
    
#     print(g)


from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    table = defaultdict(int)

    for num in nums:
        r = num % k
        if r != 0:
            table[k - r] += 1

    ans = 0
    for key, val in table.items():
        ans = max(ans, key + (val - 1) * k)

    print(ans + 1 if ans else 0)


t = int(input())
for _ in range(t):
    solve()