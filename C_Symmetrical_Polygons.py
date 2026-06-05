import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    freq = Counter(nums)

    pair_sum = 0
    odds = []

    # collect pairs and odds
    for x, c in freq.items():
        pair_sum += (c // 2) * x
        if c % 2 == 1:
            odds.append(x)

    odds.sort()

    ans = 0

    # Case 1: only pairs
    if pair_sum > 0:
        ans = max(ans, 2 * pair_sum)

    # Case 2: add one odd stick
    for x in odds:
        ans = max(ans, 2 * pair_sum + x)

    # Case 3: add two odd sticks
    for i in range(1, len(odds)):
        ans = max(ans, 2 * pair_sum + odds[i - 1] + odds[i])

    print(ans)