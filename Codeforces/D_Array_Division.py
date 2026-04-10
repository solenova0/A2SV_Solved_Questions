from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
S = sum(arr)
if S % 2 != 0:
    print("NO")
    exit()

target = S // 2
pre = 0
lcount = Counter()
rcount = Counter(arr)

for i in range(n):
    pre += arr[i]
    rcount[arr[i]] -= 1
    if rcount[arr[i]] == 0:
        del rcount[arr[i]]
        
    lcount[arr[i]] += 1
    
    if pre == target:
        print("YES")
        exit()
    
    if pre > target:
        need = pre - target
        if lcount.get(need, 0) > 0:
            print("YES")
            exit()
    
    else:
        need = target - pre
        if rcount.get(need, 0) > 0:
            print("YES")
            exit()
print("NO")