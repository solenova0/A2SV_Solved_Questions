import sys
input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
left = 0
curr = 0

for right in range(n):
    curr += a[right]            
    while curr > s:             
        curr -= a[left]
        left += 1
    ans += right - left + 1           

print(ans)