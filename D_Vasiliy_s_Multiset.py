class Node:
    def __init__(self):
        self.child = [None, None]
        self.cnt = 0

root = Node()

def insert(x):
    node = root
    for i in range(30, -1, -1):
        b = (x >> i) & 1
        if node.child[b] is None:
            node.child[b] = Node()
        node = node.child[b]
        node.cnt += 1

def remove(x):
    node = root
    for i in range(30, -1, -1):
        b = (x >> i) & 1
        node = node.child[b]
        node.cnt -= 1

def query(x):
    node = root
    ans = 0
    for i in range(30, -1, -1):
        b = (x >> i) & 1
        want = 1 - b
        if node.child[want] and node.child[want].cnt > 0:
            ans |= (1 << i)
            node = node.child[want]
        else:
            node = node.child[b]
    return ans

insert(0)

q = int(input())
for _ in range(q):
    op, x = input().split()
    x = int(x)

    if op == "+":
        insert(x)
    elif op == "-":
        remove(x)
    else:
        print(query(x))