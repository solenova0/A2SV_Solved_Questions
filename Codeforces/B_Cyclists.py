import sys, math, itertools, heapq
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from functools import cmp_to_key
from operator import itemgetter
from random import randint

input = sys.stdin.readline

intinput  = lambda: int(input())
strinput  = lambda: input().strip()
listinput = lambda: list(map(int, input().split()))
tupleinput= lambda: tuple(map(int, input().split()))
mapinput  = lambda: map(int, input().split())
matrixintinput = lambda n: [listinput() for _ in range(n)]
matrixstrinput = lambda n: [input().split() for _ in range(n)]

num, arr, word = intinput, listinput, strinput
words = lambda: input().split()

yn = lambda c: "YES" if c else "NO"

RANDOM = randint(1, 2**32 - 1)
xor = lambda x: x ^ RANDOM

test_cases = lambda d=0: intinput() if d == 0 else d

def solve():
        n, k, p, m =mapinput()
        a = arr()
        p -= 1  
        deck = deque(a)
        
        ans = 0
        energy = m
        
        while True:
            found = False
            for i in range(min(k, len(deck))):
                if i == p:
                    found = True
                    break
            
            if found:
                if energy >= deck[p]:
                    energy -= deck[p]
                    ans += 1
                    
                    val = deck[p]
                    del deck[p]
                    deck.append(val)
                    
                    p = len(deck) - 1
                else:
                    break
            else:
                idx = -1
                mn = 10**9
                
                for i in range(k):
                    if deck[i] < mn:
                        mn = deck[i]
                        idx = i
                
                if energy < mn:
                    break
                
                energy -= mn
                val = deck[idx]
                del deck[idx]
                deck.append(val)
                
                if idx < p:
                    p -= 1
                elif idx == p:
                    p = len(deck) - 1
        print(ans)

for _ in range(test_cases()):
    solve()