# t = int(input())
# for _ in range(t):
#     n , k = map(int,input().split())
#     arr  = []
#     for i in range(n):
#         v =  [int(i) for i in input().split()]
#         arr.append(v)
#     arr.sort()
#     for i in  (arr):
#         if i[0] <= k  and   i[2]  > k:
#             k =  i[2]
#     print(k)
def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        s = input().strip()
        
        if len(set(s)) == 1:
            print(n)
            continue
        
        count = 0
        
        for i in range(n):
            l, r = 0, n - 1
            ok = True
            
            while l < r:
                if l == i:
                    l += 1
                if r == i:
                    r -= 1
                
                if l < r and s[l] != s[r]:
                    ok = False
                    break
                
                l += 1
                r -= 1
            
            if ok:
                count += 1
        
        print(count)

solve()