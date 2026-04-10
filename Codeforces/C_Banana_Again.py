n = int(input())
w = list(map(int, input().split()))
total = sum(w)
diff = float('inf')

def backtrack(i, sum1):
    global diff
    if i == n:
        sum2 = total - sum1
        diff = min(diff, abs(sum1 - sum2))
        return
    backtrack(i + 1, sum1 + w[i])
    backtrack(i + 1, sum1)

backtrack(0, 0)
print(diff)