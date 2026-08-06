from sys import setrecursionlimit
setrecursionlimit(1 << 25)
class Node:
    def __init__(self):
        self.child = [None, None]

def add(root, x):
    node = root
    for i in range(29, -1, -1):
        b = (x >> i) & 1
        if node.child[b] is None:
            node.child[b] = Node()
        node = node.child[b]

def get(root, x):
    node = root
    ans = 0
    for i in range(29, -1, -1):
        b = (x >> i) & 1
        if node.child[b]:
            node = node.child[b]
        else:
            ans |= 1 << i
            node = node.child[b ^ 1]
    return ans

def solve(arr, bit):
    if bit < 0 or len(arr) <= 1:
        return 0

    left = []
    right = []

    for x in arr:
        if (x >> bit) & 1:
            right.append(x)
        else:
            left.append(x)

    ans = solve(left, bit - 1) + solve(right, bit - 1)

    if left and right:
        trie = Node()
        for x in left:
            add(trie, x)

        best = 1 << 60
        for x in right:
            best = min(best, get(trie, x))
        ans += best + (1 << bit)

    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(a, 29))