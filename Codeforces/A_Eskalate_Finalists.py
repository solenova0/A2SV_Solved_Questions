K = int(input())
ranks = list(map(int, input().split()))
ans = 0
for r in ranks:
    ans = max(ans, r - 25)
ans = max(0, ans)

print(ans)