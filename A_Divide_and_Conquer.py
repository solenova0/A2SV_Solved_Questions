for _ in range(int(input())):
    x, y = map(int, input().split())
    print("YES" if x % y == 0 else "NO")