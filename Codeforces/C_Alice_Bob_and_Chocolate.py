n = int(input())
t = list(map(int, input().split()))
l, r = 0, n - 1

timeA, timeB = 0, 0
countA, countB = 0, 0

while l <= r:
    if timeA <= timeB:
        timeA += t[l]
        l += 1
        countA += 1
    else:
        timeB += t[r]
        r -= 1
        countB += 1

print(countA, countB)