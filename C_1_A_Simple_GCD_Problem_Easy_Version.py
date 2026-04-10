import sys
import math
def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    
    res = []
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = [int(x) for x in input[ptr : ptr + n]]
        ptr += n
        ptr += n 
        
        ops = 0
        adj_gcd = []
        for i in range(n - 1):
            adj_gcd.append(math.gcd(a[i], a[i+1]))
            
        for i in range(n):
            if i == 0:
                required_gcd = adj_gcd[0]
            elif i == n - 1:
                required_gcd = adj_gcd[n-2]
            else:
            
                left_g = adj_gcd[i-1]
                right_g = adj_gcd[i]
                required_gcd = math.lcm(left_g, right_g)
            
            if required_gcd < a[i]:
                ops += 1              
        res.append(str(ops))
    
    sys.stdout.write("\n".join(res) + "\n")

if __name__ == "__main__":
    solve()
    