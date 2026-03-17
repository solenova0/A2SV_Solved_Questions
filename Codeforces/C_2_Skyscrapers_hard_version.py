t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_best = [0]*n
    stack = []
    for i in range(n):
        height = arr[i]
        while stack and stack[-1][0] > height:
            stack.pop()
        if not stack:
            left_best[i] = height*(i+1)
        else:
            prev_height, prev_pos = stack[-1]
            left_best[i] = left_best[prev_pos] + height*(i - prev_pos)
        stack.append((height, i))

    # Right-to-left profile
    right_best = [0]*n
    stack = []
    for i in range(n-1, -1, -1):
        height = arr[i]
        while stack and stack[-1][0] > height:
            stack.pop()
        if not stack:
            right_best[i] = height*(n - i)
        else:
            prev_height, prev_pos = stack[-1]
            right_best[i] = right_best[prev_pos] + height*(prev_pos - i)
        stack.append((height, i))

    # Combine both sides for each potential peak
    ans = 0
    for i in range(n):
        total = left_best[i] + right_best[i] - arr[i]
        ans = max(ans, total)

    print(ans)