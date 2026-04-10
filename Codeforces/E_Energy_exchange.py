n, k = map(int, input().split())
a = list(map(float, input().split()))
loss = (100 - k) / 100.0
def myfun(x):
    curr = 0.0
    need = 0.0
    
    for v in a:
        if v > x:
            curr += (v - x)
        else:
            need += (x - v)
    
    return curr * loss >= need

low, high = 0.0, max(a)
for _ in range(100):  
    mid = (low + high) / 2
    if myfun(mid):
        low = mid
    else:
        high = mid

print(low)