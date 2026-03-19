from collections import Counter
import sys
def intgr():
    return int(sys.stdin.readline())
def ilist():
    return list(map(int, sys.stdin.readline().split()))
def solve():
    n = intgr()
    points = [ilist() for _ in range(n)]

    cnt = Counter()
    ans = 0

    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            key = (xi + xj, yi + yj)
            ans += cnt[key]
            cnt[key] += 1

    print(ans)

def main():
    solve()

if __name__ == "__main__":
    main()