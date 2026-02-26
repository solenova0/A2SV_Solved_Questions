n = int(input())

towers = []
blocks = []

for _ in range(n):
    tower = list(map(int, input().split()))
    
    tower_size = tower[0]        
    tower = tower[1:]            
    
    towers.append(tower)
    blocks.extend(tower)

sorted_blocks = sorted(blocks)

block_rank = {}
for i in range(len(sorted_blocks)):
    block_rank[sorted_blocks[i]] = i

splits = 0
for tower in towers:
    for i in range(len(tower) - 1):
        if block_rank[tower[i + 1]] != block_rank[tower[i]] + 1:
            splits += 1

combines = n + splits - 1

print(splits, combines)