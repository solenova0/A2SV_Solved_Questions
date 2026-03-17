testcase = int(input())
for _ in range(testcase):
    n = int(input())
    nums = list(map(int, input().split()))
    
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            print("YES")
            break
    else:
        print("NO")




testcase = int(input())

for _ in range(testcase):
    n = int(input())
    S = input()
    
    count = 0
    for i in range(n - 1, -1, -1):
        if S[i] != ')':
            break
        count += 1
    
    if count > n - count:
        print("Yes")
    else:
        print("No")