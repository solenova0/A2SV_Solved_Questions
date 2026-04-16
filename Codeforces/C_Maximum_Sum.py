for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    curr_sum = 0
    max_sum = float('-inf')
    
    for i in range(n):
        curr_sum += a[i]
        max_sum = max(max_sum, curr_sum)
        
        if curr_sum < 0:
            curr_sum = 0

    MOD = 10**9 + 7
    max_sum = max(0, max_sum)
    ans = (sum(a) + (pow(2, k, MOD) - 1) * max_sum) % MOD
    
    print(ans)