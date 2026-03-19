n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = j = 0
ans = 0

while i < n and j < m:
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        val = a[i]
        
        cntA = 0
        while i < n and a[i] == val:
            cntA += 1
            i += 1
        
        cntB = 0
        while j < m and b[j] == val:
            cntB += 1
            j += 1
        
        ans += cntA * cntB

print(ans)