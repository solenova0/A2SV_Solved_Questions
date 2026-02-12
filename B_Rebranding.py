# n , m = map(int, input().split())
# s = list(input())
# for _ in range(m):
#     x,y = map(str,input().split())
#     for i in range(n):
#         if s[i] == x:
#             s[i] = y
#         elif s[i] == y:
#             s[i] = x

# print ("".join(s))
n, m = map(int, input().split())
s = input()

freq = {chr(i): chr(i) for i in range(97, 123)}

for _ in range(m):
    x, y = input().split()
    
    for k in freq:
        if freq[k] == x:
            freq[k] = y
        elif freq[k] == y:
            freq[k] = x
temp = []

for c in s:
    temp.append(freq[c])

print( ''.join(temp))
