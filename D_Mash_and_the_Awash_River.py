# from collections import Counter
# t = int(input())
# for _ in range(t):
#     s = input()
#     if "**" in s or ">*" in s or "*<" in s  or "><" in s:
#         print(-1)
#     elif len(s) == 1:
#         print(1)
#     else:
#        count = Counter(s)
#        n = len(s)
#        res = n - min(count[">"], count["<"])
#        print(res)


# t = int(input())
# for _ in range(t):
#     river = input()
#     flag = False
#     for i in range(len(river)-1):
#         if (river[i] == "*" and river[i + 1] == "*") or (river[i] == "*" and river[i + 1] == "<"):
#             flag = True
#         if (river[i] == ">" and river[i + 1] == "<") or (river[i] == ">" and river[i + 1] == "*"):
#             flag = True

#     if flag:
#         print(-1)
#     else:

#         less , great = 0 , 0
#         for i in river:
#             if i != "<": 
#                 less+=1
#             if i != ">":
#                 great += 1
#         print(max(less , great))
t = int(input())
for _ in range(t):
    s = input()
    if '**' in s or '*<' in s or '>*' in s or '><' in s:
        print(-1)
 
    else:
       max_ = 0
       for i in range(len(s)):
           if s[i] == '<':
               max_ = max(max_, i + 1)
        
           elif s[i] == '>':
               max_ = max(max_, len(s) - i)
        
           else:
            max_ = max(max_, i + 1, len(s) - i)
    
       print(max_)