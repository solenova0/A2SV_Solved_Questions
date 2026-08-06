from math import isqrt
n = int(input())
nums = list(map(int, input().split()))

max_ = 10**6

prime = [True] * (max_ + 1)
prime[0] = prime[1] = False

for i in range(2, isqrt(max_) + 1):
    if prime[i]:
        for j in range(i * i, max_ + 1, i):
            prime[j] = False

for x in nums:
    r = isqrt(x)

    if r * r == x and prime[r]:
        print("YES")
    else:
        print("NO")