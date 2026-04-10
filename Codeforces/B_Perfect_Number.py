def count_perfect(x):
    count = 0
    for num in range(1, x+1):
        if sum(int(d) for d in str(num)) == 10:
            count += 1
    return count

k = int(input())
low, high = 1, 10**9  
ans = -1

while low <= high:
    mid = (low + high) // 2
    if count_perfect(mid) >= k:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)