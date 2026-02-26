n , m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
 

for k in range(m):
    while i < n and a[i] < b[k]:
        i += 1  
    print(i, end=' ')
        
