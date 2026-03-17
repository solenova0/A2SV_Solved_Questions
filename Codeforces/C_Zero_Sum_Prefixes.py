from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    permutation = deque(map(int, input().split()))

    is_beautiful = ['0'] * n
    is_beautiful[n - 1] = '1'  

    min_popped = float('inf')

    for num in range(n - 2, -1, -1):
        if permutation[0] > permutation[-1]:
            min_popped = min(min_popped, permutation.popleft())
        else:
            min_popped = min(min_popped, permutation.pop())

        if min_popped > num + 1:   
            is_beautiful[num] = '1'

    print("".join(is_beautiful))