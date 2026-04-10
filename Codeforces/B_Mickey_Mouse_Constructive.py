import sys

def count_divisors(n):
    n = abs(n)
    if n == 0: return 1
    cnt = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            cnt += 1
            if i*i != n:
                cnt += 1
    return cnt

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    t = int(input[0])
    pointer = 1
    results = []
    
    MOD = 676767677
    
    for _ in range(t):
        x = int(input[pointer])
        y = int(input[pointer+1])
        pointer += 2
        
        total_sum = x - y
        
        if total_sum == 0:
            results.append("1")
            results.append(" ".join(["1"] * x + ["-1"] * y))
        else:
            val = count_divisors(total_sum) % MOD
            results.append(str(val))
            
            if x >= y:
                results.append(" ".join(["1"] * x + ["-1"] * y))
            else:
                results.append(" ".join(["-1"] * y + ["1"] * x))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()