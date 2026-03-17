import sys
from math import gcd
input = sys.stdin.readline
def lcm(x, y):
    return x * y // gcd(x, y)

t = int(input())
for _ in range(t):
    a, b, c, m = map(int, input().split())
    ab = lcm(a, b)
    ac = lcm(a, c)
    bc = lcm(b, c)
    abc = lcm(ab, c)

    A = m // a
    B = m // b
    C = m // c

    AB = m // ab
    AC = m // ac
    BC = m // bc
    ABC = m // abc

    A_only = A - AB - AC + ABC
    B_only = B - AB - BC + ABC
    C_only = C - AC - BC + ABC

    AB_only = AB - ABC
    AC_only = AC - ABC
    BC_only = BC - ABC

    alice = 6*A_only + 3*AB_only + 3*AC_only + 2*ABC
    bob   = 6*B_only + 3*AB_only + 3*BC_only + 2*ABC
    carol = 6*C_only + 3*AC_only + 3*BC_only + 2*ABC

    print(alice, bob, carol)