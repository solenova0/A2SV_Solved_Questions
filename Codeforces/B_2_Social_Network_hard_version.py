from collections import deque
def solve(n, k, messg):
    solve = deque()
    seen = set()

    for id_i in messg:
        if id_i not in seen:
            if len(solve) == k:
                removed = solve.pop()
                seen.remove(removed)
            
            solve.appendleft(id_i)
            seen.add(id_i)

    print(len(solve))
    print(*solve)


n, k = map(int, input().split())
messg = list(map(int, input().split()))

solve(n, k, messg)