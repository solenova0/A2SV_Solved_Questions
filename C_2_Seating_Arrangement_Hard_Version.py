t = int(input())
for _ in range(t):
    n, tables, seats = map(int, input().split())
    seats -= 1
    people = input().strip()

    empty = tables      
    ambi = 0           
    free = 0            
    ans = 0

    for p in people:
        if p == 'I':
            if empty:
                empty -= 1
                free += seats
                ans += 1
            elif ambi:
                if free:
                    free -= 1
                    ans += 1
                free += seats
                ambi -= 1

        elif p == 'E':
            if free:
                free -= 1
                ans += 1
            elif ambi:
                ambi -= 1
                free += seats
                if free:
                    free -= 1
                    ans += 1

        else:  # 'A'
            if empty:
                empty -= 1
                ambi += 1
                ans += 1
            elif free:
                free -= 1
                ans += 1

        while ambi and not free:
            free += seats
            ambi -= 1

    print(ans)