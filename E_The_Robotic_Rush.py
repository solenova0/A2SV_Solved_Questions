t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    robots = list(map(int,input().split()))
    spikes = set(map(int,input().split()))
    instr = input().strip()
    
    alive = n
    move = 0
    pos = robots[:]
    
    alive_set = set(pos)
    
    res = []
    
    for c in instr:
        if c == 'R':
            move += 1
        else:
            move -= 1
        
        dead = set()
        for r in alive_set:
            if r + move in spikes:
                dead.add(r)
        alive_set -= dead
        res.append(len(alive_set))
    
    print(*res)
