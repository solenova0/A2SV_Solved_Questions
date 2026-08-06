n, k = map(int, input().split())
s = input().strip()

def solve(ch):
    l = 0
    cnt = 0
    ans = 0

    for r in range(n):
        if s[r] != ch:
            cnt += 1
        while cnt > k:
            if s[l] != ch:
                cnt -= 1
            l += 1
        ans = max(ans, r - l + 1)

    return ans

print(max(solve('a'), solve('b')))