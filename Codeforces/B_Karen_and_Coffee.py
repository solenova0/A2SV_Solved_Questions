import sys
input = sys.stdin.readline

MOD = 10**9 + 7
BASE = 91138233

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        
        # If all same → all valid
        if len(set(s)) == 1:
            print(n)
            continue
        
        # Precompute powers
        pw = [1] * (n + 1)
        for i in range(n):
            pw[i+1] = pw[i] * BASE % MOD
        
        # Prefix hash
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = (pref[i] * BASE + ord(s[i])) % MOD
        
        # Reverse string
        rs = s[::-1]
        
        # Prefix hash for reversed string
        rpref = [0] * (n + 1)
        for i in range(n):
            rpref[i+1] = (rpref[i] * BASE + ord(rs[i])) % MOD
        
        # Get hash of substring s[l:r]
        def get_hash(pref, l, r):
            return (pref[r] - pref[l] * pw[r-l]) % MOD
        
        count = 0
        
        for i in range(n):
            # hash of s without i
            left_hash = get_hash(pref, 0, i)
            right_hash = get_hash(pref, i+1, n)
            
            new_hash = (left_hash * pw[n-i-1] + right_hash) % MOD
            
            # same for reversed
            # index in reversed = n-1-i
            ri = n - 1 - i
            
            left_hash_r = get_hash(rpref, 0, ri)
            right_hash_r = get_hash(rpref, ri+1, n)
            
            new_hash_r = (left_hash_r * pw[n-ri-1] + right_hash_r) % MOD
            
            if new_hash == new_hash_r:
                count += 1
        
        print(count)

solve()