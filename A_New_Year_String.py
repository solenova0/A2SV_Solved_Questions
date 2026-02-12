# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = input()

#     if "2025" not in s:
#         print(0)
#         continue

#     b = float('inf')
#     for i in range(n-3):
#         c = 0
#         if s[i] != '2':
#             c += 1
#         if s[i+1] != '0':
#             c += 1
#         if s[i+2] != '2':
#             c += 1
#         if s[i+3] != '6':
#             c += 1
#         if c < b:
#             b = c

#     v = 0
#     for i in range(n-3):
#         if s[i:i+4] == "2025":
#             v += 1

#     if b < v:
#         print(b)
#     else:
#         print(v)
t = int(input())
for _ in range(t):
   n = int(input())
   s = input()
   if '2025' not in s or '2026' in s:
      print(0)
   else:
      print(1)