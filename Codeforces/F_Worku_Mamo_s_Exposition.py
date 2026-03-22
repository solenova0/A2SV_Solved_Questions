from collections import deque
n, k = map(int, input().split())
h = list(map(int, input().split()))

maxD = deque()
minD = deque()
left = 0
maxx = 0
dur = []

for right in range(n):
    while maxD and h[maxD[-1]] <= h[right]:
        maxD.pop()
    maxD.append(right)
    
    while minD and h[minD[-1]] >= h[right]:
        minD.pop()
    minD.append(right)
    
    while h[maxD[0]] - h[minD[0]] > k:
        left += 1
        if maxD[0] < left:
            maxD.popleft()
        if minD[0] < left:
            minD.popleft()
    
    curr = right - left + 1
    if curr > maxx:
        maxx = curr
        dur = [(left + 1, right + 1)]  
    elif curr == maxx:
        dur.append((left + 1, right + 1))

print(maxx, len(dur))
for a, b in dur:
    print(a, b)