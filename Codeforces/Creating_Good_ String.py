def calc(l, r, c):
    if l == r:
        if s[l] == c:
            return 0
        return 1
    
    mid = (l + r) // 2
    
    left_changes = (mid - l + 1) - s[l:mid + 1].count(c)    
    left_result = left_changes + calc(mid + 1, r, chr(ord(c) + 1))
 
    right_changes = (r - mid) - s[mid + 1:r + 1].count(c)
    right_result = right_changes + calc(l, mid, chr(ord(c) + 1))
 
    return min(left_result, right_result)
 
for _ in range(int(input())):
    n = int(input())
    s = input()
 
    print(calc(0, len(s) - 1, 'a'))