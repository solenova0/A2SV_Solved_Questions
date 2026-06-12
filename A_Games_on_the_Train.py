for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    
    print(max(h) - min(h) + 1)