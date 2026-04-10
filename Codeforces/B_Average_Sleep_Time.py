n , k = map(int,input().split())
arr = list(map(int, input().split()))
window = sum(arr[:k])
total = window
for i in range(k,n):
    window += arr[i]
    window -= arr[i-k]
    total += window
print(total / (n - k + 1))