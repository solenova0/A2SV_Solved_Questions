from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))

pref = []
s = 0

for x in a:
    s += x
    pref.append(s)

m = int(input())
q = list(map(int, input().split()))

for x in q:
    print(bisect_left(pref, x) + 1)