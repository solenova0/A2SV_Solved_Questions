class Node:
    def __init__(self):
        self.child = {}
        self.end = False

root = Node()

def insert(word):
    cur = root
    for c in word:
        if c not in cur.child:
            cur.child[c] = Node()
        cur = cur.child[c]
    cur.end = True

def dfs(node, s, i, changed):
    if i == len(s):
        return changed and node.end

    for c in "abc":
        if c in node.child:
            if c == s[i]:
                if dfs(node.child[c], s, i + 1, changed):
                    return True
            elif not changed:
                if dfs(node.child[c], s, i + 1, True):
                    return True
    return False

n, m = map(int, input().split())

for _ in range(n):
    insert(input())

for _ in range(m):
    print("YES" if dfs(root, input(), 0, False) else "NO")