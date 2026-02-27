import math
def solve(arr):
    n = len(arr)
    ans = float('inf')
    prev = []  

    for i in range(n):
        curr = []
        curr.append((arr[i], i))

        for g, idx in prev:
            new = math.gcd(g, arr[i])

            if curr[-1][0] == new:
                curr[-1] = (new, min(curr[-1][1], idx))
            else:
                curr.append((new, idx))

        for g, idx in curr:
            if g == 1:
                ans = min(ans, i - idx + 1)

        prev = curr

    return -1 if ans == float('inf') else ans
n = int(input())
arr = list(map(int, input().split()))
print(solve(arr))