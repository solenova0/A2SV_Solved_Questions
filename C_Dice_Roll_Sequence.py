adjacent = {
    1: [2,3,4,5],
    2: [1,3,4,6],
    3: [1,2,5,6],
    4: [1,2,5,6],
    5: [1,3,4,6],
    6: [2,3,4,5]
}

t = int(input())  

for _ in range(t):
    n = int(input())  # length of the sequence
    sequence = list(map(int, input().split()))
    
    operations = 0
    prev_val = sequence[0]  # start with the first number
    
    for i in range(1, n):
        curr_val = sequence[i]
        if curr_val in adjacent[prev_val]:
            # no change needed
            prev_val = curr_val
        else:
            # change current to an adjacent number
            operations += 1
            prev_val = adjacent[prev_val][0]  # pick first adjacent for simplicity
    
    print(operations)
